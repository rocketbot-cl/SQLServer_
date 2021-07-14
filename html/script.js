function addOptions(spsGot) {
    console.log("Cuando pasa esto?")
    var select = document.getElementById("spsGot")
    for (spGot of spsGot) {
        var opt = document.createElement('option');
        opt.value = spGot;
        opt.innerHTML = spGot;
        select.appendChild(opt);
        if (spGot.toLowerCase() == document.spsGot_spGot) {
            opt.selected = true
        }
    }

}

data = getDataFromRB({module_name:"SQLServer_", command_name:"getHtmlSps"})
.then(data => {
    spsGot = data["spsGot"]
    addOptions(spsGot)
})

