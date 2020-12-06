$(document).ready(function (){
    let place_image_div = $("#place_image_div");
    let place_image = $("#place_image");

    let loading_message = $("<div class='loading'>Image is loading, wait...</div>");

    $(".event").on("click", function (e){
        let point = $(this).data('point');
        if (point){
            url = "https://api.mapbox.com/styles/v1/mapbox/streets-v11/static/pin-s-embassy+f74e4e(" +
                point + ")/" +
                point + " ,14.25,0,60/600x600?access_token="+ mapboxgl.accessToken;

            place_image.attr('src', url);
            place_image_div.append(loading_message);
            place_image.on("load",function (){
                $(".loading").remove();
            });

            place_image_div.css({
                "visibility": "visible",
            });

            $("body").append("<div id='shadow'></div>");
            $("#shadow").on("click", function (e){
                place_image_div.css({
                    "visibility": "hidden",
                });
                $(this).remove();
                place_image.removeAttr('src');
            });

        }
    });
});