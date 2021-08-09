document.getElementById("add-row").addEventListener("click", function(){
    table.addRow({});
});
document.getElementById("clear").addEventListener("click", function(){
    table.clearData()
});

// data = getDataFromRB({module_name:"odbc", command_name:"get_drivers"})
// .then(data => {
//     drivers = data["drivers"]
// })

