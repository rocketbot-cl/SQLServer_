# testing/schema.py
# Copyright (C) 2005-2021 the SQLAlchemy authors and contributors
# <see AUTHORS file>
#
# This module is part of SQLAlchemy and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

from . import config
from . import exclusions
from .. import event
from .. import schema
from .. import types as sqltypes


__all__ = ["Table", "Column"]

table_options = {}


def Table(*args, **kw):
    """A schema.Table wrapper/hook for dialect-specific tweaks."""

    test_opts = {k: kw.pop(k) for k in list(kw) if k.startswith("test_")}

    kw.update(table_options)

    if exclusions.against(config._current, "mysql"):
        if (
            "mysql_engine" not in kw
            and "mysql_type" not in kw
            and "autoload_with" not in kw
        ):
            if "test_needs_fk" in test_opts or "test_needs_acid" in test_opts:
                kw["mysql_engine"] = "InnoDB"
            else:
                kw["mysql_engine"] = "MyISAM"
    elif exclusions.against(config._current, "mariadb"):
        if (
            "mariadb_engine" not in kw
            and "mariadb_type" not in kw
            and "autoload_with" not in kw
        ):
            if "test_needs_fk" in test_opts or "test_needs_acid" in test_opts:
                kw["mariadb_engine"] = "InnoDB"
            else:
                kw["mariadb_engine"] = "MyISAM"

    # Apply some default cascading rules for self-referential foreign keys.
    # MySQL InnoDB has some issues around selecting self-refs too.
    if exclusions.against(config._current, "firebird"):
        table_name = args[0]
        unpack = config.db.dialect.identifier_preparer.unformat_identifiers

        # Only going after ForeignKeys in Columns.  May need to
        # expand to ForeignKeyConstraint too.
        fks = [
            fk
            for col in args
            if isinstance(col, schema.Column)
            for fk in col.foreign_keys
        ]

        for fk in fks:
            # root around in raw spec
            ref = fk._colspec
            if isinstance(ref, schema.Column):
                name = ref.table.name
            else:
                # take just the table name: on FB there cannot be
                # a schema, so the first element is always the
                # table name, possibly followed by the field name
                name = unpack(ref)[0]
            if name == table_name:
                if fk.ondelete is None:
                    fk.ondelete = "CASCADE"
                if fk.onupdate is None:
                    fk.onupdate = "CASCADE"

    return schema.Table(*args, **kw)


def Column(*args, **kw):
    """A schema.Column wrapper/hook for dialect-specific tweaks."""

    test_opts = {k: kw.pop(k) for k in list(kw) if k.startswith("test_")}

    if not config.requirements.foreign_key_ddl.enabled_for_config(config):
        args = [arg for arg in args if not isinstance(arg, schema.ForeignKey)]

    col = schema.Column(*args, **kw)
    if test_opts.get("test_needs_autoincrement", False) and kw.get(
        "primary_key", False
    ):

        if col.default is None and col.server_default is None:
            col.autoincrement = True

        # allow any test suite to pick up on this
        col.info["test_needs_autoincrement"] = True

        # hardcoded rule for firebird, oracle; this should
        # be moved out
        if exclusions.against(config._current, "firebird", "oracle"):

            def add_seq(c, tbl):
                c._init_items(
                    schema.Sequence(
                        _truncate_name(
                            config.db.dialect, tbl.name + "_" + c.name + "_seq"
                        ),
                        optional=True,
                    )
                )

            event.listen(col, "after_parent_attach", add_seq, propagate=True)
    return col


class eq_type_affinity(object):
    """Helper to compare types inside of datastructures based on affinity.

    E.g.::

        eq_(
            inspect(connection).get_columns("foo"),
            [
                {
                    "name": "id",
                    "type": testing.eq_type_affinity(sqltypes.INTEGER),
                    "nullable": False,
                    "default": None,
                    "autoincrement": False,
                },
                {
                    "name": "data",
                    "type": testing.eq_type_affinity(sqltypes.NullType),
                    "nullable": True,
                    "default": None,
                    "autoincrement": False,
                },
            ],
        )

    """

    def __init__(self, target):
        self.target = sqltypes.to_instance(target)

    def __eq__(self, other):
        return self.target._type_affinity is other._type_affinity

    def __ne__(self, other):
        return self.target._type_affinity is not other._type_affinity


def _truncate_name(dialect, name):
    if len(name) > dialect.max_identifier_length:
        return (
            name[0 : max(dialect.max_identifier_length - 6, 0)]
            + "_"
            + hex(hash(name) % 64)[2:]
        )
    else:
        return name