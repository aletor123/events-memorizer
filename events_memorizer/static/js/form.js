$(document).ready(function (){
    let form_div = $("#form_div");
    $("#add_new_event").on("click", function (e){
        form_div.css({
            "visibility": "visible",
        });
        $("body").append("<div id='shadow'></div>");
        $("#shadow").on("click", function (e){
            form_div.css({
                "visibility": "hidden",
            });
            $(this).remove();
        });
    });
});