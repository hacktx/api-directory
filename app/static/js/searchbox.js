$(document).ready(function() {
    // change input text color appropriately
    $('#search').focus(function(e) {
        $(this).removeClass('white-text');
    }).blur(function(e) {
        $(this).addClass('white-text');
    });
});
