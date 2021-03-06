$(function() {
    $.slidebars();


    /* ######################################

    Centering vertically the contact labels

    ###################################### */
    var $frame = $('.contact li .back');
    $frame.css('position', 'relative');

    $frame.each(function() {
        var $p = $(this).find('p');
        $p.css('top', ($(this).innerHeight() - $p.innerHeight()) / 2 )
            .css('left', ($(this).innerWidth() - $p.innerWidth()) / 2)
            .css('width', $p.innerWidth())
            .css('margin-top', '0')
            .css('position', 'absolute');
    });

    /* ######################################

    Biography script

    ###################################### */
    $(".biography").hover(function(e) {
        if ($(this).find('img').length > 1) {
            $(this).find('img').stop();
            $(this).find('img').fadeToggle(200);
        }
    });
});
