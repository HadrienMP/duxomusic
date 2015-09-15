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
});