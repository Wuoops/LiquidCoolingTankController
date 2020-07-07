var pueCharts = echarts.init(document.getElementById('pue'));

function pueJs(){
    pueCharts.setOption({
    series : [
        {
            name: '访问来源',
            type: 'pie',
            radius: '55%',
            data:[
                {value:2.15, name:'IT Power'},
                {value:0.5, name:'Orther Power'},
            ]
        }
    ]
    })
}
pueJs()
