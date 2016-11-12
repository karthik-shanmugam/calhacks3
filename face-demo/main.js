$(document).ready(function() {
    Webcam.attach( '#my_camera' );

    function take_snapshot() {
        Webcam.snap( function(data_uri) {
            document.getElementById('my_result').innerHTML = '<img src="'+data_uri+'"/>';
            $("emotion-img").attr("src", "");
            post("/image", {'image': data_uri}, function(data){
                document.getElementById('temp').innerHTML = data_uri;
                switch (data) {
                    case "happiness":
                        $(".emotion-img").attr("src", "emojis/smile.png");
                        break;
                    case "sadness":
                        $(".emotion-img").attr("src", "emojis/frown.png");
                        break;
                    default:
                        $(".emotion-img").attr("src", "emojis/neutral.png");
                }       
                console.log(data);
            });
        });
    }

    $(".snap").click(take_snapshot);

    function post(path, parameters, callback) {
        var form = $('<form></form>');

        form.attr("method", "post");
        form.attr("action", path);

        $.each(parameters, function(key, value) {
            var field = $('<input></input>');

            field.attr("type", "hidden");
            field.attr("name", key);
            field.attr("value", value);

            form.append(field);
        });

        // The form needs to be a part of the document in
        // order for us to be able to submit it.
        $.ajax({
            url:'/image',
            type:'post',
            data:form.serialize(),
            success:callback
        });
        // $(document.body).append(form);
        // form.submit();
        console.log("submitted")
    }    
})
