//document.write('Hello World');
//document.write('<h1>Welcome to JS program</h1>');
//document.write('<h2>Welcome to JS Program</h2>');
//
//console.log('Welcome JS program');
//console.info('Welcome JS program');
//console.warn('Welcome JS program');
//console.error('error JS program');
//
//alert('Welcome JS Program'); //쓰지 말자
//var a = prompt('Welcome JS Program'); //변수 입력 받기 가능
//console.log(a);

//console.log(typeof 123);
//console.log(typeof 123.4);
//console.log(typeof '하이');
//console.log(typeof !123);
//console.log(typeof 'asd');
//console.log(typeof true);
//console.log(true, typeof true);

//var car
//console.log(typeof car);
//car = ''
//console.log(typeof car);
//var person = {firstName : 'jin', lastName: 'lee', age: 50, eyeColor: 'blue'};
//console.log(typeof person, person);
//person = null;
//console.log(typeof person, person);

//var name = '이승훈';
//var age = 29;
//var cgpa = 3.92;
//var lineBrake = '<br/>'
//
//document.write("이름: "+name+lineBrake);
//document.write("나이: "+age+lineBrake);
//document.write("학점: "+cgpa+lineBrake);

//var lastName = '홍';
//var firstName = '길동';
//var fullName = lastName + firstName;
//
//console.log(fullName);
//console.log("Today"+'good');
//console.log('My name is'+fullName);
//
//var num1 = 20;
//var num2 = 30;
//console.log(num1+num2)
//console.log(''+num1+num2)

//var text = prompt("Enter your name:")
//document.write("Your name:" +text+ "</br>");
//
//var len = text.length;
//document.write("number of characters:"+len+"</br>");
//document.write(text.charAt(0)+"</br>");
//document.write(text.toUpperCase()+"</br>");
//document.write(text.toLowerCase()+"</br>");

//var text1 = 'h1';
//var text2 = 'bye';
//var text3 = text1.concat(text2);
////var text4 = text1 + text2;
//var text4 = "hello";
//document.write(text3 + "<br/>");
//document.write(text4 + "<br/>");
//
//var result = text4.slice(0,2);
//document.write(result+"<br/>");

//var numStr = "20";
//console.log(typeof numStr);
//numStr = numStr.toString();
//console.log(typeof numStr);
//
//var number = 20;
//console.log(typeof number);
//number = toString(20);
//console.log(typeof number);

//var x = 2.45345;
//console.log(x.toFixed(1));
//console.log(x.toFixed(2));
//
//console.log(x.toPrecision(1), typeof x.toPrecision(1));
//console.log(x.toPrecision(2));
//
//console.log(Number(true));
//console.log(Number(false));
//console.log(Number(" 10"));
//console.log(Number("10.25"));

//var num1 = parseInt(prompt("Enter first number: "));
//var num2 = parseInt(prompt("Enter second number: "));
var lineBreak = "</br>";
//
//var result = num1 + num2;
//document.write("the sum : "+ result + lineBreak);
//
//result = num1 - num2;
//document.write("the sub :" + result + lineBreak);
//
//result = num1 * num2;
//document.write("the mul :" + result + lineBreak);
//
//result = num1 / num2;
//document.write("the div :" + result + lineBreak);
//
//result = num1 % num2;
//document.write("the rem :" + result + lineBreak);

var base = parseInt(prompt("밑변"))
var height = parseInt(prompt("높이"))
document.write("삼각형 넓이 :" + base*height*0.5 + lineBreak);