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

//IIFE 예제
(function display(message){
    console.log(message);
})("hi");

//var display2 = function displayMessage(msg){
//    console.log(msg)
//}
//console.log(typeof display2)
//display2("display2 message");

(function addNum(a , b){
    console.log(a + b);
})(3,5);