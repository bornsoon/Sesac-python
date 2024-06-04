function sayHello() {
    console.log('Hello');
}
function sayPrint() {
    print();
}

console.log('콘솔로그') //콘솔창에 로고를 출력한다.
document.write('Hello, World'); //문서에 글자를 쓴다.
document.write('<P>');
document.write('헬로우 어게인');
document.write('<H2>헤딩 추가하기</H2>');   // document가 새로 안만들어지고 추가되는 이유는 DOM이 만들어지는 과정에서(끝에서가 아니라) write 했기때문에...

for(var i = 1; i <= 5; i++) {
    document.write("<H3>숫자: " + i + "</H3>")
}