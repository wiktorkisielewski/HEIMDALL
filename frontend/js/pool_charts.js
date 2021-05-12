var pool_depth = {
  labels: ["1", "2", "3", "4", "6", "7"],
  datasets: [{
    label: "Pool Depth",
    backgroundColor: "rgba(107,225,208,0.2)",
    borderColor: "rgba(107,225,208,0.2)",
    borderWidth: 2,
    hoverBackgroundColor: "rgba(107,225,208,0.2)",
    hoverBorderColor: "rgba(107,225,208,0.2)",
    data: [65, 59, 20, 81, 56, 55, 40],
  }]
};

var price = {
  labels: ["1", "2", "3", "4", "6", "7"],
  datasets: [{
    label: "Price",
    backgroundColor: "rgba(107,225,208,0.2)",
    borderColor: "rgba(107,225,208,0.2)",
    borderWidth: 2,
    hoverBackgroundColor: "rgba(107,225,208,0.2)",
    hoverBorderColor: "rgba(107,225,208,0.2)",
    data: [21, 33, 37, 42, 27, 33, 36],
  }]
};

var options = {
  maintainAspectRatio: false,
  scales: {
    yAxes: [{
      stacked: true,
      gridLines: {
        display: true,
        color: "rgba(107,225,208,0.2)"
      }
    }],
    xAxes: [{
      gridLines: {
        display: false
      }
    }]
  }
};

Chart.Line('bnb.bnb_test_chart', {
  options: options,
  data: pool_depth
});


