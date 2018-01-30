$(function(){
	$(document).ready(function($){
		$('.scroll').on('click', function(event){
			event.preventDefault();
			$('html,body').animate({scrollTop:$(this.hash).offset().top -105}, 300);
		});
	});
	$('#menumobile').on('click', function (){
		$('.menu').show();
	});
	$('#closemenubtn').on('click', function (){
		$('.menu').hide();
	});
	$(window).scroll(function (){
		var currentScrollTop = $(window).scrollTop();

	$('#black-overlay').css('opacity',currentScrollTop/$('#black-overlay').height());
		});
})(jQuery);