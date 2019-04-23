-============JQUERY============-
=========Селекторы=========
	$('*')	Будут выбраны все элементы присутствующие на странице.
	$("#el1")	Будет выбран элемент с id=el1
	$(".el1")	Будут выбраны все элементы на странице с class=el1.
	$("div")	Будут выбраны все элементы div на странице.
	$("div, #el1, .el1")	Будут выбраны все элементы div, элемент с id="el1" и все элементы с 							class="el1" на странице.
	$("[src]")	Будут выбраны все элементы на странице имеющие атрибут src.
	$(":input")	Будут выбраны все элементы input на странице.
=========Обработчики событий=========
	on('click, hover', function ) - можно выбрать несколько обработчиков
	click - произведён щелчок по объекту.
	dblclick - произведён двойной щелчок по объекту.
	focus - объект получает фокус.
	keypress - пользователь нажимает клавишу клавиатуры и удерживает её в нажатом состоянии
	mousedown - пользователь нажал клавишу мыши.
	mouseup - пользователь отпускает нажатую клавишу мыши.
	mousemove - пользователь перемещает курсор мышью.
	mouseout - когда указатель мыши покидает определенную область.
	mouseover - указатель мыши проходит над объектом или областью.
	scroll - изменяются размеры области просмотра документа.
	submit - пользователь отправляет форму на сервер.
	unload - пользователь выходит из документа (закрывает страницу).
	hover(over, out) - отслеживание попадания указателя мыши в пределы объекта
	setTimeout(func, 4000) - функция произойдет через промедуток указанный параметром
	setInterval - функция будет повторяться постоянно через определенный промежутьок времени
	setInterval(function() {}, 100);
=========DOM=========
	$("").after("<p></p>"); - вставляет содержимое после элемента
	html() -
	before() - вставляет указанное содержимое перед выбранным элементом.
	children('selector') - возвращает все элементы помки указанного элемента.
=========Методы CSS манипулирования=========
	addClass() - Добавляет указанный класс или классы выбранному элементу.
	toggleClass() - добавление или удаление класса в зависимости от текущего состояния
	css() - Позволяет узнать текущее или установить новое значение указанному CSS свойству
			(или свойствам) выбранного элемента.
		$("").css({"top":"5px", "left":"0"})
	hasClass() - Проверяет содержит ли выбранный элемент класс с указанным именем.
    removeClass() -	Удаляет у выбранного элемента один класс или более.
    $(' ').text()  - change text
	$(' ').html() - change html
	$(' ').append()  - add some text after current text
	$(' ').prepand()  - addd text before current text
	$(' ').after()  - new element after
	$(' ').wrap()  - add container element
	$(' ').unwrap()  - delete container element
	$(' ').empty()  - make element empty
	$(' ').remove()  - remove element
=========Эффекты jQuery=========
	fadeIn(2000) - Постепенно меняет прозрачность выбранного элемента делая его видимым.
							(1000 миллисекунд = 1 секунда)
	fadeOut(2000) -
	hide(1500)
	show(1500)
	$("div").fadeOut().delay(2000).fadeIn(); - задержка
=========Остальное=========
	val() - получить значение элемента формы
	preventDeafault() - отменяется стандартные функции у элемент

=========Анимация jQuery=========
	$("селектор").animate({стили},скорость,функция_смягчения,функция);
	функция_смягчения задает функцию, которая будет отвечать за плавность выполнения анимации.
	функция указывает имя функции, код которой будет выполнен после завершения анимации.
$(document).ready(function(){

	$("#but1").click(function(){
		$("p").animate({fontSize:30},2000);
	});

});


========AJAX========
$.ajaxSetup({
     beforeSend: function(xhr, settings) {
         function getCookie(name) {
             var cookieValue = null;
             if (document.cookie && document.cookie != '') {
                 var cookies = document.cookie.split(';');
                 for (var i = 0; i < cookies.length; i++) {
                     var cookie = jQuery.trim(cookies[i]);
                     // Does this cookie string begin with the name we want?
                     if (cookie.substring(0, name.length + 1) == (name + '=')) {
                         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                         break;
                     }
                 }
             }
             return cookieValue;
         }
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     }
});

Синтаксис:
var data = {};
var url = form.attr("action");
$.ajax({
	url: url,
	type: 'POST',
	data: data,
	dataType: 'json',
	success: function (response) {
		console.log("success");
    },
    error: function () {
		console.log('Error');
	}
});
