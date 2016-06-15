$(document).ready(function() {
	$('a.link').click( function(event){ // click by link
		var link_adr = $(this).attr("href");
		$("iframe").attr("src",link_adr);
		event.preventDefault(); // disable standard role element
		$('#overlay').fadeIn(100, 
		 	function(){ // after the previous animation
				$('#modal_form') 
					.css('display', 'block') // remove from the modal window display: none;
					.animate({opacity: 1, height: '100%', position: 'absolute',
					top: '0%', left: 0, right: 0 }, 0);
														
		});
	});
	/* Closing a modal window, then we do the same but in reverse order */
	$('#modal_close').click( function(){ // click by link 
		$('#modal_form')
			.animate({opacity: 0, top: '45%'}, 200,  
				function(){ // after animation
					$(this).css('display', 'none'); // display: none;
				}
			);
	});
});

$(document).ready(function() {
	$('li.response').click( function(e){
		e.preventDefault();
		var view = $(this).attr("id");
		$('li.response').removeClass('active');
		$(this).addClass('active');
		$('#forma').attr("class",view)
	});
});

