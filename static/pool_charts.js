var options = {
  maintainAspectRatio: false,
  elements: {
    point:{
        radius: 0
    }
  },
  scales: {
    yAxes: [{
      stacked: false,
      gridLines: {
        display: true,
        color: "#FFFFFF70"
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
      position: "bottom",
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
  data = '0';
  result = py_test(data);
  console.log('py_test ok' + data)
});


function plot_it(chart_data) {
  Chart.defaults.global.defaultFontColor="#FFFFFF90";
  Chart.Line('test_chart', {
  options: options,
  data: chart_data
});
}