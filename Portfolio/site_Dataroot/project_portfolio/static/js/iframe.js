$(document).ready(function() {
	$('a.link').click( function(event){ // ловим клик по ссылки
		var link_adr = $(this).attr("href");
		$("iframe").attr("src",link_adr);
		event.preventDefault(); // выключаем стандартную роль элемента
		$('#overlay').fadeIn(0, // сначала плавно показываем темную подложку
		 	function(){ // после выполнения предъидущей анимации
				$('#modal_form') 
					.css('display', 'block') // убираем у модального окна display: none;
					.animate({opacity: 1, height: '100%', position: 'absolute',
					top: '0%', left: 0, right: 0 }, 0); // плавно прибавляем прозрачность одновременно со съезжанием вниз
		});
	});
	/* Закрытие модального окна, тут делаем то же самое но в обратном порядке */
	$('#modal_close').click( function(){ // ловим клик по крестику или подложке
		$('#modal_form')
			.animate({opacity: 0, top: '45%'}, 200,  // плавно меняем прозрачность на 0 и одновременно двигаем окно вверх
				function(){ // после анимации
					$(this).css('display', 'none'); // делаем ему display: none;
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
