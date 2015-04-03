$(function() {
    $.slidebars();

    /*$('form.ajax').submit(function(event) {

        var parent = $(this).parent();
        parent.css("position","relative");
        var $overlay = $('<div style="position:absolute; top: 0; left: 0; bottom: 0; width: 100%; background: rgba(100,100,100,0.8);"><i class="fa fa-spinner fa-pulse"></i></div>');
        parent.append($overlay);

        event.preventDefault();
        var url = $(this).attr('action');
        $.ajax({
            type : "POST",
            url : url,
            data : $(this).serialize(),
            success : function(data) {
                alert(data);
                $overlay.remove();
            },
            error : function(data) {
                alert(data);
            }
        });
    });*/
});
