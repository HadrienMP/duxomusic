$(function() {
    $('#disqus_thread').hide();
    $('.show-disqus').click(function () {
        $('#disqus_thread').slideToggle();
        $(this).find('i').toggleClass('fa-caret-right').toggleClass('fa-caret-down');

        var $span = $(this).find('span');
        var afficher = 'Afficher';
        var cacher = 'Cacher';
        if ($span.text() === afficher) {
            $span.text(cacher);
        } else {
            $span.text(afficher);
        }

    });
    
    $('.block.sound iframe').each(function() {
       $(this).height($(this).height() * $(this).parent().innerWidth() / $(this).width());
       $(this).width($(this).parent().innerWidth() - 1);
    });
});