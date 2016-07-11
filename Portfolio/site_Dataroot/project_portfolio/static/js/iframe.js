var phantom = function(view){
	var idClass = '.';
	var idIframe = idClass + view;
	var widthIframe = $(idIframe).css("width");
	var heightIframe = $(idIframe).css("height");
	$('.status_width').html(widthIframe.slice(0,-2));
    $('.status_height').html(heightIframe.slice(0,-2));
}

var report = function(view){
	var idClass = '.';
	var idIframe = idClass + view;
	var widthIframe = $(idIframe).css("width");
	var heightIframe = $(idIframe).css("height");

	$(idIframe).css({"width": heightIframe, "height": widthIframe });
}


$(document).ready(function() {
	$('li.response').click( function(e){
		e.preventDefault();
		$('#wrapper').attr("style", "");
		var view = $(this).attr("id");
		$('li.response').removeClass('active');
		$(this).addClass('active'); 
		$('#wrapper').attr("class",view);
		$('#phantom').attr("class",view);
		phantom(view);
		//$('#wrapper').css({"transition": "all 150ms cubic-bezier(.5,0,1,1)"});
		var viewId = $('li.response.active img').attr("id");
		var strId = '#';
		var idOp = strId + viewId;
		$('li.response.active').hover( function(){
			$(idOp).removeClass('hover_');
			elem = document.getElementById("wrapper");
			if (elem.className == view && view != 'autosize') {
				$(idOp).addClass('hover_in');
				$('.hover_in').click( function(){
					//var view = $("li.response.active").attr("id");
					//var idClass = '.';
					//var idIframe = idClass + view;
					//var widthIframe = $(idIframe).css("width");
					//var heightIframe = $(idIframe).css("height");
					//$(idIframe).css({"width": heightIframe, "height": widthIframe });
					//$(idOp).attr("style", "");
					$(idOp).toggleClass("hover_li");
				});
			}

		}, function() {
			$(idOp).removeClass('hover_in');
		});
	});
	$('.menu_profile').click( function(){
		$('.sidebar').addClass('asidebar');
		$('.close').click( function(){
			$('.sidebar').removeClass('asidebar');
		});
	});

	$('.close_out').click( function(){
		window.history.back();
	});

	$('li.response').hover(function(){
			$('#phantom').attr("style", "");
			var view = $(this).attr("id");
	    	$('#phantom').toggleClass(view);
	    });

});

window.onload=function() {
	document.getElementById("wrapper").style.height= document.body.scrollHeight;
}


$(function(){
    var prev_x = -1;
    var prev_y = -1;
    var dir = null;
  $("#wrapper > b").mousedown(function(e){
        prev_x = e.clientX;
        prev_y = e.clientY;
        dir = $(this).attr('id');
    });
    
    $(document).mousemove(function(e){
        if (prev_x == -1)
            return;
        
        var boxX = $("#wrapper").position().left;
        var boxY = $("#wrapper").position().top;
        var boxW = $("#wrapper").width();
        var boxH = $("#wrapper").height();
        var dx = e.clientX - prev_x;
        var dy = e.clientY - prev_y;
        
        //Check directions
        if (dir.indexOf('n') > -1) //north
        {
            boxY += dy;
            boxH -= dy;
        }
        if (dir.indexOf('s') > -1) //south
        {
            boxH += dy;
        }
        if (dir.indexOf('w') > -1) //west
        {
            boxX += dx;
            boxW -= dx;
        }
        if (dir.indexOf('e') > -1) //east
        {
            boxW += dx;
        }
            
        $("#wrapper").css({
            "width":(boxW)+"px",
            "height":(boxH)+"px",
        });

        $('.status_width').html(Math.round(boxW));
        $('.status_height').html(Math.round(boxH));
        
        $("#phantom").css({
            "width":(boxW)+"px",
            "height":(boxH)+"px",
        });
        
        prev_x = e.clientX;
        prev_y = e.clientY;
    });
    
    $(document).mouseup(function(){
        prev_x = -1;
        prev_y = -1;
    });
});

