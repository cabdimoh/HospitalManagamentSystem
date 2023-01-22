am5.ready(function() {

// Create root element
// https://www.amcharts.com/docs/v5/getting-started/#Root_element
var root = am5.Root.new("chartdiv");


// Set themes
// https://www.amcharts.com/docs/v5/concepts/themes/
root.setThemes([
  am5themes_Animated.new(root)
]);


// Create chart
// https://www.amcharts.com/docs/v5/charts/xy-chart/
var chart = root.container.children.push(am5xy.XYChart.new(root, {
  panX: true,
  panY: true,
  wheelX: "panX",
  wheelY: "zoomX",
  pinchZoomX:true
}));

// Add cursor
// https://www.amcharts.com/docs/v5/charts/xy-chart/cursor/
var cursor = chart.set("cursor", am5xy.XYCursor.new(root, {}));
cursor.lineY.set("visible", false);


// Create axes
// https://www.amcharts.com/docs/v5/charts/xy-chart/axes/
var xRenderer = am5xy.AxisRendererX.new(root, { minGridDistance: 30 });
xRenderer.labels.template.setAll({
  rotation: -90,
  centerY: am5.p50,
  centerX: am5.p100,
  paddingRight: 15
});

var xAxis = chart.xAxes.push(am5xy.CategoryAxis.new(root, {
  maxDeviation: 0.3,
  categoryField: "country",
  renderer: xRenderer,
  tooltip: am5.Tooltip.new(root, {})
}));

var yAxis = chart.yAxes.push(am5xy.ValueAxis.new(root, {
  maxDeviation: 0.3,
  renderer: am5xy.AxisRendererY.new(root, {})
}));


// Create series
// https://www.amcharts.com/docs/v5/charts/xy-chart/series/
var series = chart.series.push(am5xy.ColumnSeries.new(root, {
  name: "Series 1",
  xAxis: xAxis,
  yAxis: yAxis,
  valueYField: "value",
  sequencedInterpolation: true,
  categoryXField: "country",
  tooltip: am5.Tooltip.new(root, {
    labelText:"{valueY}"
  })
}));

series.columns.template.setAll({ cornerRadiusTL: 5, cornerRadiusTR: 5 });
series.columns.template.adapters.add("fill", function(fill, target) {
  return chart.get("colors").getIndex(series.columns.indexOf(target));
});

series.columns.template.adapters.add("stroke", function(stroke, target) {
  return chart.get("colors").getIndex(series.columns.indexOf(target));
});


// Set data
var data = [{
  country: "Civid19",
  value: 2500
}, {
  country: "Cancer",
  value: 1882
}, {
  country: "Influence",
  value: 1809
}, {
  country: "Headache",
  value: 2000
}, {
  country: "Malaria",
  value: 1600
}, {
  country: "Gasteric ",
  value: 1400
}, {
  country: "Floza",
  value: 1800
// },
}];

xAxis.data.setAll(data);
series.data.setAll(data);


// Make stuff animate on load
// https://www.amcharts.com/docs/v5/concepts/animations/
series.appear(1000);
chart.appear(1000, 100);

}); // end am5.ready()
const ctx = document.getElementById('myChart').getContext('2d');
const myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Perchased service', 'Staff salery/benifits', 'Supplies', 'Interest Exp', 'Bad depart', 'taxes'],
      datasets: [{
        label: ' It Cost %',
        data: [11.3, 51, 15.9, 6.8, 2.5, 3.5],
        backgroundColor: [
          'rgba(71, 160, 255, 1)',
          'rgba(111, 123, 236, 1)',
          'rgba(254, 157, 76, 1)',
          'rgba(90, 170, 90, 1)',
          'rgba(46, 94, 1, 1)',
          'rgba(0, 0, 0, 1)',
            ],
            borderColor: [
                'rgba(71, 160, 255, 1)',
                'rgba(111, 123, 236, 1)',
                'rgba(254, 157, 76, 1)',
                'rgba(90, 170, 90, 1)',
                'rgba(46, 94, 1, 1)',
                'rgba(255, 255, 255, 1)',
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});


var btn1 = document.getElementById("btnOne")
var el = document.documentElement;
btn1.addEventListener("click", () => {
  if (el.requestFullscreen) {
    el.requestFullscreen();
  }  
})
btn1.addEventListener("click", () => {
  if (document.exitFullscreen) {
    document.exitFullscreen();
  }
})