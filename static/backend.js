function analyze () {

    const message = document.getElementById('enter').value;

    // Check if text is empty   
    if (message == "") {
        return undefined
    }

    var inputs_obj = {
        message : message
    }

    $.ajax({
        type : "POST",
        url : "/",
        contentType: "application/json",
        dataType : "json",
        data :JSON.stringify(inputs_obj),
        encode : true,
        success : function (data) {
            console.log(data)
        }
    })
}