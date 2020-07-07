var cpuChart = echarts.init(document.getElementById('cpuMaxTemp'));

var cpudd = []
var serListCpu = []

//CPU部分
setTimeout(function () {
    cpuChart.hideLoading();
    getData();

    option = {
        legend: {},
        tooltip: {
            trigger: 'axis',
//            showContent: false
        },
        dataset: {
            source: cpudd
        },
        xAxis: {type: 'category'},
        yAxis: {gridIndex: 0},
//        grid: {top: '55%'},
        series: serListCpu
    };
    cpuChart.setOption(option);
},1000);

function getcpuData(){
    $.ajax({
        url: '/getcpuData/',
        type: 'POST',
        data:{},
//        async:false
        success: function(data){
            cpudd.push(data)
            serListCpu = []
            for (i = 1;i<data.data.length;i++){
                  b = {type: 'bar',  seriesLayoutBy: 'row'}
                  serListCpu.push(b)
            }
                cpuChart.setOption({
                    dataset: {
                        source: data.data
                    },
                    series : serListCpu
                });
        }
    })
}
//
setInterval(function () {
//在此处执行获取数据的方法
    getcpuData();
}, 1000);


