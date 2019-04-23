// ########### HIGHCHARTS ###########
// installation
// basic
<script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
<script src="https://code.highcharts.com/stock/highstock.js"></script>
// additional modules
<script src="https://code.highcharts.com/stock/modules/exporting.js"></script>

var options = {}
$(function () {
    Highcharts.stockChart('container', options);
});

// OPTIONS
// ============================
title: {}
    text: 'text'
// ============================
subtitle: {}
    text: 'subtitle text'
// ============================
chart: {}  // base chart options
    backgroundColor: ''
    borderColor: ''
    borderRadius: 1
    events: {}  // chart events listener
        load: function (){}  // fires when chart is loaded but before render
        render: function (){}  // fires when chart is rendered
// ============================
rangeSelector: {}
    buttons: [{type: 'day', count: 3, text: '3 days'}]
    selected: 1
// ============================
plotOptions : {series: {}} // general setting for all series
    allowPointSelect: boolean // select by clicking on candle(or other graphic)
    cursor: 'pointer'
    colors: []  // array of specific colors for this series
    selected: bool  //
    events: {}  // event handler for series item
        click: function(){}
        mouseOver: function(){}
        mouseOut: function(){}
    tooltip: {}  // appears when hovering a point
        padding: 1
        headerFormat: ''
        footerFormat: ''
    zones: [{}]
    zIndex: 1

plotOptions: {series: {dataGrouping: {units: [['hour', [1]]]}}},
// ============================
series: {}  //
    type: 'candlestick'
    allowPointSelect: boolean // select by clicking on candle(or other graphic)
    cursor: 'pointer'
    selected: bool  // ???
    dataGrouping: {}
    keys: []  // array specifying which option points which key in data array
    name: '' // name that will be shown in tooltip, legend
    softTrreshold: 'try true' // !!!!
    events: {}  // event handler for series item
        click: function(){}
        mouseOver: function(){}
        mouseOut: function(){}
    tooltip: {}  // appears when hovering a point
        padding: 1
        headerFormat: ''
        footerFormat: ''
    zones: [{}]
// ============================
xAxis: {}
yAxis: {}
    title: 'title'
    subtitle: 'subtitle'
    gridLineWidth: 1
    crosshair: {}  // line folows mouse
// ============================
annotations: [{}]  // options for labels, arrows, shapes
    labelOptions: {},
    labels: [{
        point: {
            xAxis: 0,
            yAxis: 0,
            x: value,
            y: value
        },
        text: str,
    }
// ============================
credits: {}  // credits label
    enabled: bool
// ============================
// ############################
// CHART CLASS METHODS
chart.update({}) // update options object after rendering
chart.addSeries({})  // add new series after rendering
chart.redraw()
// Series method
series = chart.series;
series = chart.series[0]; // append data in the begining
series.addPoint(new_data, redraw=true, shift=true)


