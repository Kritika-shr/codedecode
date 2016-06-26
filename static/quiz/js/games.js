// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


$(document).ready(function(){
    var csrftoken = getCookie('csrftoken');
    $("#btnguess").click(function(){

        event.preventDefault();
        console.log("form submitted!")  // sanity check
        create_post();
        //Post this data to django view for further processing

    });

    // AJAX for posting
    function create_post() {

        //This Has to be here
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });
        var csrftoken = getCookie('csrftoken');
        guess=$("#guess").val()
        console.log("create post is working!") // sanity check
        $.ajax({
            url:"/games/create_post/",
            type:"POST",
            data:{guess:guess},
            success:function(result){
                console.log("Success");
                console.log(result);
            },
            error:function(err){
                console.log("Error");
            }

        });
    };

    });
