$(function () {
    $('[data-toggle="tooltip"]').tooltip();
    $('.percent-value span').each(function() {
        var numAnim = new countUp(this, 0, $(this).text());
        numAnim.start();
    });

    window.setTimeout(function() {
        var data = {
            labels: ids,
            datasets: [
                {
                    label: "Recipients",
                    fillColor: "rgba(220,220,220,0.5)",
                    strokeColor: "rgba(220,220,220,0.8)",
                    highlightFill: "rgba(220,220,220,0.75)",
                    highlightStroke: "rgba(220,220,220,1)",
                    data: recipients
                },
                {
                    label: "Readers",
                    fillColor: "rgba(151,187,205,0.5)",
                    strokeColor: "rgba(151,187,205,0.8)",
                    highlightFill: "rgba(151,187,205,0.75)",
                    highlightStroke: "rgba(151,187,205,1)",
                    data: readers
                }
            ]
        };

        var ctx = document.getElementById("trend").getContext("2d");
        var options = {
            'bezierCurve' : false,
        }
        var chart = new Chart(ctx).Line(data, options);
    }, 100);
});