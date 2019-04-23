// -============ JAVASCRIPT ============-

// NUMBER
    var some_number = Number(x);
// мягкое преобразование parseInt и parseFloat;
	var some_value = parseInt('12px');
    Math.round();
	var some_integer = Math.round(x);

// STRING

// length
    var some_string = 'some string';
    var string_length = some_string.length;
// substring
    var substring = some_string.substring(3, 5)
//split
    some_string.split(', ') // вернет массив
    some_string.split('') // по буквам

// OBJECTS
// словарь

///////////////////////////////////////////////////////////
// ARRAYS
    var some_array = new Array(8)
    var some_array = []

    some_array[5] = 'smth';
    var new_var = some_array[2]

    // methods
        arr.pop() // удалит последний элемент
        arr.push(something) // добавит элемент в конец массива
        arr.forEach() //

// for loop
	for (var i = 0; i < arr.length; i++) {
  		alert( arr[i] );
	}
// length()
	var arrays_length = length(some_array);

========Functions========
function showMessage() {
	return ;
};
showMessage();

if (text === undefined) {
	text = 'текст не передан';
}else {
  }

while (n < 3) {
  n++;
  x += n;
}


// built-in functions
typeof var;

========Classes========
    class User {

        constructor(name) {
            this.name = name;
        }
    }


============ Math ========

Math.ceil(int) - округляет число к большему
Math.floor(int) - округляет число к меньшему
Math.round(int) - округляет к большему или меньшему по правилу
Math.abs(int) - модуль
