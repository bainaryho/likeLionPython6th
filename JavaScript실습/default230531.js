//var br = "<br/>"
//// 매개변수가 없는 함수 생성하기
//function hello(){
//    document.write("Hello. function without param"+br);
//}
//
//// 한개의 매개변수가 있는 함수 생성
//function welcomeMessage(name){
//    document.write("welcome "+name+br);
//}
//
////두개의 매개변수가 있는 함수 생성
//function addition(num1, num2){
//    var sum = num1 + num2;
//    document.write("addtion is "+ sum + br);
//}
//
//function square(num){
//    return num * num;
//}
//
//hello();
//welcomeMessage("이진호");
//addition(1,3);
//document.write("square of 5 is " + square(5)+br);

////IIFE 예제
//(function display(message){
//    console.log(message);
//})("hi");
//
////var display2 = function displayMessage(msg){
////    console.log(msg)
////}
////console.log(typeof display2)
////display2("display2 message");
//
//(function addNum(a , b){
//    console.log(a + b);
//})(3,5);

////배열
//var names = new Array(20);
//names[0] = "지훈";
//names[1] = "은영";
//console.log(names);
//console.log(names[1]);
//
////값을 가진 배열 생성
//var students = ['지훈','은영','수진'];
//console.log('students = ', students);
//console.log('2번 인덱스 = ', students[2]);
//
////배열의 길이 찾기
//console.log(students.length);
//
////배열의 요소 추가
//students.push('정민');
//console.log('추가 후 students = ', students);
//
////배열 요소 삭제
//students.pop();
//console.log('pop후 학생 배열 = ',students);
//
////배열 연결 하기
//var numArray1 = [10, 20];
//var numArray2 = [30, 40, 50, 60];
//var numArray = numArray1.concat(numArray2);
//var whattype = numArray1 + numArray2
//
//console.log('배열 잇기 concat : '+numArray);
//console.log(typeof numArray);
//
//console.log('배열 잇기 + : '+numArray1 + numArray2);
//console.log(typeof whattype);

var date = new Date();
console.log(date);

var year = date.getFullYear();
console.log(year);

var month = date.getMonth();
console.log(month);

var currentDate = date.getDate();
console.log(currentDate);

var currentDay = date.getDay();
console.log(currentDay);

var currentHour = date.getHours();
console.log(currentHour);

var currentMinutes = date.getMinutes();
console.log(currentMinutes);