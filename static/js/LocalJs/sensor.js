var myChart = echarts.init(document.getElementById('main'));
var sensorData = []
var serList = []
var sensorline = 100

myChart.showLoading();
setTimeout(function () {

    myChart.hideLoading();
    getSensorData();

    option = {
        legend: {},
        tooltip: {
            trigger: 'axis',
//            showContent: false
        },
        dataset: {
            source: sensorData
        },
        xAxis: {type: 'category'},
        yAxis: {gridIndex: 0},
//        grid: {top: '55%'},
        series: serList
    };



    myChart.setOption(option);



},1000);
function getSensorData(){
    $.ajax({
        url: '/getSensorData/',
        type: 'POST',
        data:{'line':sensorline},
//        async:false
        success: function(data){
            sensorData.push(data)
            serList = []
            for (i = 1;i<data.data.length;i++){
                  a = {type: 'line', smooth: true, seriesLayoutBy: 'row'}
                  serList.push(a)
            }
                myChart.setOption({
                    dataset: {
                        source: data.data
                    },
                    series : serList

                });
        }
    })
}
//
setInterval(function () {
//在此处执行获取数据的方法
    getSensorData();
}, 1000);


function changeLines(){
    a = document.getElementById('lines').value
    if (a){
        sensorline = a
    }
}
