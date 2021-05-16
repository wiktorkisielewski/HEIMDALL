var chart_data = {
  labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
  datasets: [{
    label: "Pool Depth",
    backgroundColor: "#54FFD820",
    borderColor: "#54FFD820",
    borderWidth: 2,
    hoverBackgroundColor: "#54FFD820",
    hoverBorderColor: "#54FFD820",
    data: [49, 47, 51, 48, 45, 44, 40, 42, 47, 45],
  },
  {
    label: "Price",
    backgroundColor: "#54FFD840",
    borderColor: "#54FFD840",
    borderWidth: 2,
    hoverBackgroundColor: "#54FFD840",
    hoverBorderColor: "#54FFD840",
    data: [11, 9, 7, 10, 9, 12, 16, 15, 18, 22],
  },
  {
    label: "Rune Depth",
    backgroundColor: "#54FFD860",
    borderColor: "#54FFD860",
    borderWidth: 2,
    hoverBackgroundColor: "#54FFD860",
    hoverBorderColor: "#54FFD860",
    data: [32, 35, 33, 31, 29, 34, 35, 37, 36, 34],
  }
  ]
};



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

function plot_it(ticker) {
  console.log(ticker)
  Chart.Line('test_chart', {
  options: options,
  data: chart_data
});
}