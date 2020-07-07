var lv = 100
$(document).ready(function() {

	$('.waterTankHere1').waterTank({
		width: 280,
		height: 300,
		color: 'skyblue',
		level: lv
	});
});
setInterval(function () {
    $.ajax({
            url: '/getLevel/',
            type: 'POST',
            data:{},
    //        async:false
            success: function(data){
                lv = data
            }
    })
    $('.waterTankHere1').waterTank({
		level: lv
	});
}, 1000);
