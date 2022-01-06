function analyze () {

    const message = document.getElementById('enter').value;
    const button = document.getElementById('button')

    button.disabled = true;

    // Check if text is empty   
    if (message == "") {

        button.disabled = false;
        return undefined;
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

            data_to_map = data.data;

            const button = document.getElementById('button')
            const div = document.getElementById("placeholder")
            var html_to_append = ""

            console.log(data_to_map.length)

            if (data_to_map.length == 0) { // If there's no response

                button.disabled = false;
                div.innerHTML = " No aspect found !"

                return undefined;
            }

            data_to_map.map(function (data) {

                html_to_append = html_to_append + "<p>"+data.aspect.toString()+ "</p>"
            })

            div.innerHTML = html_to_append
            button.disabled = false;
        }
    })
}