var options = {
  maintainAspectRatio: false,
  scales: {
    yAxes: [{
      stacked: false,
      gridLines: {
        display: true,
        color: "#54FFD855"
      }
    }],
    xAxes: [{
      gridLines: {
        display: false
      }
    }]
  },
  legend: {
      display: true,
      position: "bottom"
    },
};

function py_test(input) {
  var jqXHR = $.ajax({
            type: "POST",
            url: "/py_test",
            async: false,
            data: { mydata: input }
        });
  return jqXHR.responseText;
}

$('#py_test').click(function() {
  data = 'BNB.BNB';
  result = py_test(data);
  console.log('py_test ok' + data)
});


function plot_it(chart_data) {
  Chart.Line('test_chart', {
  options: options,
  data: chart_data
});
}