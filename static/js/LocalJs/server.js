var serverChart = echarts.init(document.getElementById('serverData'));

var dd = []
var serList = []
var nodeSelect = 0
var serverLines = 100
var nodeNum = document.getElementById('serverName').innerHTML
serverChart.showLoading();
setTimeout(function () {
    serverChart.hideLoading();
    getData();

    option = {
        legend: {},
        tooltip: {
            trigger: 'axis',
//            showContent: false
        },
        dataset: {
            source: dd
        },
        xAxis: {type: 'category'},
        yAxis: {gridIndex: 0},
//        grid: {top: '55%'},
        series: serList
    };
    serverChart.setOption(option);
},1000);

function getData(){
    $.ajax({
        url: '/getBmcData/',
        type: 'POST',
        data:{'line':serverLines,'node':nodeNum},
//        async:false
        success: function(data){
            dd.push(data)
            serList = []
            for (i = 1;i<data.data.length;i++){
                  a = {type: 'line', smooth: true, seriesLayoutBy: 'row'}
                  serList.push(a)
            }
                serverChart.setOption({
                    dataset: {
                        source: data.data
                    },
                    series : serList
                });
        }
    })
}

setInterval(function () {
//在此处执行获取数据的方法
    getData();
}, 1000);


function nodeChoice(id){
    document.getElementById('serverName').innerHTML = id ;
    nodeNum = id
}

function serverChangeLines(){
    b = document.getElementById('serverlines').value
    if (b){
        serverLines = b
    }
}
