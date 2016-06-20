
function phantom(view) {
	var idClass = '.';
	var idPixcel = 'px';
	var idIframe = idClass + view;
	var widthIframe = $(idIframe).css("width");
	var heightIframe = $(idIframe).css("height");
	var intWidthIframe = +widthIframe.slice(0,-2);
	var intMarginLeftPhantom = -(intWidthIframe/2);
	var marginLeftPhantom = intMarginLeftPhantom + idPixcel;
	$("#phantom").css({"width": widthIframe, "height": heightIframe,
	"margin-left": marginLeftPhantom,});
}

$(document).ready(function() {
	$('#wrapper').resizable();
	
	$('li.response').click( function(e){
		e.preventDefault();
		var view = $(this).attr("id");
		$('#phantom').removeClass('leftX');
		$('li.response').removeClass('active');
		$(this).addClass('active');
		$('#wrapper').attr("class",view)
		phantom(view);
		$('#wrapper').css({"transition": "all 150ms cubic-bezier(.5,0,1,1)"});
		var viewId = $('li.response.active img').attr("id");
		var strId = '#';
		var idOp = strId + viewId;
		$(idOp).hover( function(){
			elem = document.getElementById("wrapper");
			if (elem.className == view) {
				$(this).addClass('hover_in');
				$('.hover_in').click( function(){
					$(this).addClass('hover_li');
					$('.hover_in').hover( function(){
						$(this).addClass('hover_out');
					}, function(){
						$(this).removeClass('hover_out');
					});
				});
			}
			else $(this).removeClass('hover_in');
		}, function() {
			$(this).removeClass('hover_in');
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

});

window.onload=function() {
	document.getElementById("wrapper").style.height= document.body.scrollHeight;
}
