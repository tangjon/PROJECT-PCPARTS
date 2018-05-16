/* Project specific Javascript goes here. */
$(document).ready(function () {
    $('.owl-carousel').owlCarousel({
        dots: false,
        center: true,
        items: 2,
        loop: true,
        margin: 10,
        responsive: {
            600: {
                items: 7
            }
        }
    });
});