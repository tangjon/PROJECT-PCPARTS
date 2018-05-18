/* Project specific Javascript goes here. */
$(document).ready(function () {
    $('.owl-carousel').owlCarousel({
        dotsEach: 5,
        center: true,
        items: 7,
        loop: true,
        margin: 10,
        responsive: {
            600: {
                items: 7
            }
        }
    });
});