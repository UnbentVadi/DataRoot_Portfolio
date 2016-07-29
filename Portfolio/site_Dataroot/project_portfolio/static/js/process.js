$(document).ready(function() {
						   
	$('.process ul li a').click(function(){
		var toLoad = $(this).attr('href')
		$.get(toLoad, function(data){
			$('.links-list').html(data);
		});
		return false;
	});

});