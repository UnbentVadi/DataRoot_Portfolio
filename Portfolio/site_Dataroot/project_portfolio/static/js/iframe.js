
function phantom(view) {
	var idClass = '.';
	var idPixcel = 'px';
	var idIframe = idClass + view;
	var widthIframe = $(idIframe).css("width");
	var heightIframe = $(idIframe).css("height");
	var intWidthIframe = +widthIframe.slice(0,-2);
	var intMarginLeftPhantom = -(intWidthIframe/2);
	var marginLeftPhantom = intMarginLeftPhantom + idPixcel;
	$("#phantom").css({"width": widthIframe, "height": heightIframe, "margin-left": marginLeftPhantom});
}

$(document).ready(function() {
	$('li.response').click( function(e){
		e.preventDefault();
		var view = $(this).attr("id");
		$('li.response').removeClass('active');
		$(this).addClass('active');
		$('#wrapper').attr("class",view)
		phantom(view);
	});
});