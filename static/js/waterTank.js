/*!
 * jQuery 3D Watertank Plugin
 * Original author: @ajeeshvijay
 */

(function ( $ ) {
 
    $.fn.waterTank = function( options ) {
 		
        var settings = $.extend({
            color: "#6ecff6",
            level: 33
        }, options );



       	function _updateTank($that, value){

       		$that.find('._tank').fadeIn(1);
		    $that.find('._balance').stop().animate({
	        	height: $that.find('._tank').height() * ( 100 - value ) / 100 ,
	        },{ 
		    	duration: speed,  
			    step: function() { $that.find('._balance').css("overflow","visible"); }, 
			    complete: function() { $that.find('._balance').css("overflow","visible"); }
			});

	        $that.find('._filled').stop().animate({
	        	height: $that.find('._tank').height() * value / 100 ,
        		opacity: 1
	        },{ 
		    	duration: speed,  
			    step: function() { $that.find('._filled').css("overflow","visible"); }, 
			    complete: function() { $that.find('._filled').css("overflow","visible"); }
			});

			$that.find('._percentageTag').text(value + '%');

			$that.find('._reflect').stop().animate({
				height: ($that.find('._tank').height() * value / 100) / 2 + 20 ,
				bottom: -($that.find('._tank').height() * value / 100) / 2 - 20,
			},
				speed
			);


			if (value == 100) {
				$that.find('._topCircle').hide(0);
			}else{
				$that.find('._topCircle').show(0);
			}



			// setTimeout(function(){
			// 	$balance.css({
			// 		opacity: 1
			// 	});
			// }, 0);


       	}

        var tilt = {
        	'-webkit-transform' : 'rotateX(65deg) translateZ(0px)',
        	'-moz-transform' : 'rotateX(65deg) translateZ(0px)',
        	'-o-transform' : 'rotateX(65deg) translateZ(0px)',
        	transform : 'rotateX(65deg) translateZ(0px)',
        	'-moz-transform-style': 'preserve-3d',
        	'-webkit-transform-style': 'preserve-3d',
        	'transform-style': 'preserve-3d',
        }
        var speed = 600;

        // Update
        if (options % 1 === 0) {

        	// console.log(options);
		    _updateTank($(this), options);

        }else{
	        if ($(this).is(':empty')){

		        var $tank = $('<div/>').appendTo(this);
		        $tank.css({
		        	width: settings.width,
		            height: settings.height,
				    position: 'relative',
				    margin:  (settings.height/2) + 'px auto',
		        	transform: 'translate3d(0,0,0)'
		        }).addClass('_tank');



		 

		        // Balance
		        var $balance = $('<div/>').appendTo($tank);
		        $balance
		        .css({
		        	height: settings.height,
				        	background: '#f2f2f1',
		        	position: 'relative',
		        	transform: 'translateZ(0px)',
				    // opacity: .2

		        })
		        .addClass('_balance');

		        var $balanceTopCircle = $('<div/>').appendTo($balance);
		        $balanceTopCircle.css(
		        	Object.assign(
			        	{
				        	height: settings.width,
				        	width: '100%',
				        	background: '#f2f2f1',
				        	borderRadius: '50%',
				        	top: 0,
				        	marginTop: -(settings.width/2),
				        	position: 'absolute'
				        },
				        tilt
			        )
			    );

			    var $topCircle = $('<div/>').appendTo($tank);
		        $topCircle.css(
		        	Object.assign(
			        	{
				        	height: settings.width,
				        	width: '100%',
				        	background: 'rgba(255, 255, 255, .2)',
				        	borderRadius: '50%',
				        	top: 0,
				        	marginTop: -(settings.width/2),
				        	position: 'absolute',
				        	zIndex: 500,
				        	// opacity: .2,
				        	pointerEvents: 'none'
				        },
				        tilt
			        )
			    )
		        .addClass('_topCircle');

			   

		        // Waterlevel
		        var $filled = $('<div/>').appendTo($tank);
		        $filled.css({
		        	height: 0 ,
		        	position: 'relative',
		        	opacity: 0,
		        	transform: 'translate3d(0,0,0)'
		        })
		        .addClass('_filled');
		        var $filledBg = $('<div/>').appendTo($filled);
		        $filledBg.css(
		        	Object.assign(
			        	{
				        	height: '100%',
				        	width: '100%',
				        	background: settings.color,
				        	position: 'absolute',
				        	opacity: .8,
				        	zIndex: 10
				        }
			        )
			    );
		        var $percentageTag = $('<div><div/>').appendTo($filledBg);
		        $percentageTag.css(
		        	Object.assign(
			        	{
				        	position: 'absolute',
				        	right: -85,
				        	width: 70,
				        	fontSize: 17,
				        	top: -10,
				        	textAlign: 'left'
				        }
			        )
			    ).addClass('_percentageTag').text(settings.level + '%');
		        var $filledTopCircle = $('<div/>').appendTo($filled);
		        $filledTopCircle.css(
		        	Object.assign(
			        	{
				        	height: settings.width,
				        	width: '100%',
				        	background: settings.color,
				        	borderRadius: '50%',
				        	top: 0,
				        	marginTop: -(settings.width/2),
				        	position: 'absolute',
				        	overflow: 'hidden',
				        	zIndex: 10
				        },
				        tilt
			        )
			    );


			    var $canvas = $('<canvas/>').appendTo($filledTopCircle);	
			    // var $canvas = 0;	

			    $canvas.css({
			    	opacity: .8,
			    	transform: 'rotate(80deg)'
			    });


			    if ($canvas) {

			    	var canvas = $canvas.get(0),
			    	    /** @type {CanvasRenderingContext2D} */
			    	    ctx = canvas.getContext('2d'),
			    	    width = settings.width,
			    	    height = settings.width,
			    	    half_width = width >> 1,
			    	    half_height = height >> 1,
			    	    size = width * (height + 2) * 2,
			    	    delay = 30,
			    	    oldind = width,
			    	    newind = width * (height + 3),
			    	    riprad = 8,
			    	    ripplemap = [],
			    	    last_map = [],
			    	    ripple,
			    	    texture,
			    	    line_width = 1,
			    	    step = line_width * 18, 
			    	    count = height / line_width;
			    	    
			    	canvas.width = width;
			    	canvas.height = height;
			    	
			    	with (ctx) {
			    	    fillStyle = settings.color;
			    	    // fillStyle = 'skyblue';
			    	    fillRect(0, 0, width, height);
			    	    
			    	    fillStyle = '#000';
			    	    save();
			    	    rotate(-0.785);
			    	    // rotate(2);
			    	    for (var i = 0; i < count; i++) {
			    	        fillRect(-width, i * step, width * 3, line_width);
			    	    }
			    	    
			    	    restore();
			    	}
			    	
			    	texture = ctx.getImageData(0, 0, width, height);
			    	ripple = ctx.getImageData(0, 0, width, height);
			    	
			    	for (var i = 0; i < size; i++) {
			    	    last_map[i] = ripplemap[i] = 0;
			    	}
			    	
			    	/**
			    	 * Main loop
			    	 */
			    	function run() {
			    	    newframe();
			    	    ctx.putImageData(ripple, 0, 0);
			    	}
			    	
			    	/**
			    	 * Disturb water at specified point
			    	 */
			    	function disturb(dx, dy) {
			    	    dx <<= 0;
			    	    dy <<= 0;
			    	    
			    	    for (var j = dy - riprad; j < dy + riprad; j++) {
			    	        for (var k = dx - riprad; k < dx + riprad; k++) {
			    	            ripplemap[oldind + (j * width) + k] += 128;
			    	        }
			    	    }
			    	}
			    	
			    	/**
			    	 * Generates new ripples
			    	 */
			    	function newframe() {
			    	    var a, b, data, cur_pixel, new_pixel, old_data;
			    	    
			    	    var t = oldind; oldind = newind; newind = t;
			    	    var i = 0;
			    	    
			    	    // create local copies of variables to decrease
			    	    // scope lookup time in Firefox
			    	    var _width = width,
			    	        _height = height,
			    	        _ripplemap = ripplemap,
			    	        _last_map = last_map,
			    	        _rd = ripple.data,
			    	        _td = texture.data,
			    	        _half_width = half_width,
			    	        _half_height = half_height;
			    	    
			    	    for (var y = 0; y < _height; y++) {
			    	        for (var x = 0; x < _width; x++) {
			    	            var _newind = newind + i, _mapind = oldind + i;
			    	            data = (
			    	                _ripplemap[_mapind - _width] + 
			    	                _ripplemap[_mapind + _width] + 
			    	                _ripplemap[_mapind - 1] + 
			    	                _ripplemap[_mapind + 1]) >> 1;
			    	                
			    	            data -= _ripplemap[_newind];
			    	            data -= data >> 5;
			    	            
			    	            _ripplemap[_newind] = data;

			    	            //where data=0 then still, where data>0 then wave
			    	            data = 1024 - data;
			    	            
			    	            old_data = _last_map[i];
			    	            _last_map[i] = data;
			    	            
			    	            if (old_data != data) {
			    	                //offsets
			    	                a = (((x - _half_width) * data / 1024) << 0) + _half_width;
			    	                b = (((y - _half_height) * data / 1024) << 0) + _half_height;
			    	
			    	                //bounds check
			    	                if (a >= _width) a = _width - 1;
			    	                if (a < 0) a = 0;
			    	                if (b >= _height) b = _height - 1;
			    	                if (b < 0) b = 0;
			    	
			    	                new_pixel = (a + (b * _width)) * 4;
			    	                cur_pixel = i * 4;
			    	                
			    	                _rd[cur_pixel] = _td[new_pixel];
			    	                _rd[cur_pixel + 1] = _td[new_pixel + 1];
			    	                _rd[cur_pixel + 2] = _td[new_pixel + 2];
			    	            }
			    	            
			    	            ++i;
			    	        }
			    	    }
			    	}
			    	
			    	canvas.onmousemove = function(/* Event */ evt) {
			    	    disturb(evt.offsetX || evt.layerX, evt.offsetY || evt.layerY);
			    	};
			    	
			    	if (settings.level >= 0) {

			    		setInterval(run, delay);
			    		
			    		// generate random ripples
			    		var rnd = Math.random;
			    		setInterval(function() {
			    		    disturb(rnd() * width, rnd() * height);
			    		}, 700);
			    	}


			    	
			    }  

	    	    var $filledBottomCircle = $('<div/>').appendTo($filled);
	            $filledBottomCircle.css(
	            	Object.assign(
	    	        	{
	    		        	height: settings.width,
	    		        	width: '100%',
	    		        	background: settings.color,
	    		        	borderRadius: '50%',
	    		        	bottom: 0,
	    		        	marginBottom: -(settings.width/2),
	    		        	position: 'absolute',
	    		        	boxShadow: 'rgba(0, 0, 0, 0.3) 0px 15px 50px'
	    		        },
	    		        tilt
	    	        )
	    	    );

	    	    var $reflect = $('<div/>').appendTo($filled); 
	    	    $reflect.addClass('_reflect');

	    	    // console.log((settings.height * (100 - settings.level)));



	    	    $reflect.css('background', '-moz-linear-gradient(top, '+settings.color+') 0%, rgba(255,255,255,0) 100%)');
	    	    $reflect.css('background', '-webkit-linear-gradient(top, '+settings.color+' 0%,rgba(255,255,255,0) 100%)');
	    	    $reflect.css('background', 'linear-gradient(to bottom, '+settings.color+' 0%,rgba(255,255,255,0) 100%)');
	    	    $reflect.css({
	    	    	position: 'absolute',
	    	    	width: '100%',

	    	    	// height: settings.width/2,
	    	    	// bottom: -(settings.width/2),

	    	    	height: ((settings.height * (100-settings.level) / 100)),
	    	    	// bottom: -((settings.height * (100-settings.level) / 100)/2),

	    	    	opacity: .4
	    	    });
	    	    

	        }else{
	        	var $tank = $(this).find('_tank');
	        	var $balance = $(this).find('_balance');
	        	var $filled = $(this).find('_filled');
	        }

		    
	        $tank.fadeOut(0);
	        var _this = $(this)
		    setTimeout(function(){
		    	_updateTank(_this, settings.level);
		    }, 300);

        }
        
        return this;
 
    };
 
}( jQuery ));
