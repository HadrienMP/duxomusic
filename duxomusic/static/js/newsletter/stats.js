$(function () {
    $('[data-toggle="tooltip"]').tooltip();
    $('.percent-value span').each(function() {
        var numAnim = new countUp(this, 0, $(this).text());
        numAnim.start();
    });

    window.setTimeout(function() {
        var data = {
            labels: ["#06", "#07", "#08", "#09", "#10", "#11", "#12"],
            datasets: [
                {
                    label: "Recipients",
                    fillColor: "rgba(220,220,220,0.5)",
                    strokeColor: "rgba(220,220,220,0.8)",
                    highlightFill: "rgba(220,220,220,0.75)",
                    highlightStroke: "rgba(220,220,220,1)",
                    data: [65, 59, 80, 81, 56, 55, 40]
                },
                {
                    label: "Open Rate",
                    fillColor: "rgba(51,153,255,0.5)",
                    strokeColor: "rgba(51,153,255,0.8)",
                    highlightFill: "rgba(51,153,255,0.75)",
                    highlightStroke: "rgba(51,153,255,1)",
                    data: [28/65*100, 29/59*100, 50/80*100, 60/81*100, 12/56*100, 45/55*100, 33/40*100]
                },
                {
                    label: "Readers",
                    fillColor: "rgba(151,187,205,0.5)",
                    strokeColor: "rgba(151,187,205,0.8)",
                    highlightFill: "rgba(151,187,205,0.75)",
                    highlightStroke: "rgba(151,187,205,1)",
                    data: [28, 29, 50, 60, 12, 45, 33]
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