function addOptions(spsGot) {
    console.log("Cuando pasa esto?")
    var select = document.getElementById("spsGot")
    for (spGot of spsGot) {
        var opt = document.createElement('option');
        console.log("Vienen los opt")
        console.log(opt)
        opt.value = spGot;
        console.log("first")
        console.log(spsGot)
        opt.innerHTML = spGot;
        console.log("Sencond")
        console.log(spGot)
        select.appendChild(opt);
        if (spGot.toLowerCase() == document.spsGot_spGot) {
            opt.selected = true
        }
    }

}

data = getDataFromRB({module_name:"SQLServer_", command_name:"getHtmlSps"})
.then(data => {
    data["spsGot"].push("---- Select Option ----")
    spsGot = data["spsGot"]
    spsGot = spsGot.sort()
    // spsGot.reverse()
    addOptions(spsGot)
})

$('#spsGot').on('change', function (e) {
    // e.data.printer
    message.commands['spGot'] = $(this).val();
    message.commands['table'] = tabledata;
    SendMessage();
})

document.getElementById("add-row").addEventListener("click", function(){
    table.addRow({});
});
document.getElementById("clear").addEventListener("click", function(){
    table.clearData()
});
