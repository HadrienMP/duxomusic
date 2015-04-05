$(function() {
    $.slidebars();


    /* ######################################

    Centering vertically the contact labels

    ###################################### */
    var $frame = $('.contact li .back');
    $frame.css('position', 'relative');

    $frame.each(function() {
        var $p = $(this).find('p');
        $p.css('position', 'absolute')
            .css('top', ($(this).innerHeight() - $p.height()) / 2 )
            .css('left', ($(this).innerWidth() - $p.width()) / 2)
            .css('margin-top', '0');
    });


//    var $img = $('header h1 img');
//    var $imgParent = $img.parent();
//    $imgParent.css('height', $imgParent.height()).css('width', $imgParent.width());
//    $img.hide(function() {
//        $img.slideDown("slow");
//    });
});
