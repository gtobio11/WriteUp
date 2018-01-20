# Webhacking.kr No.25

## 문제 출제 의도
URL 인코딩 방식을 이용하여 문제의 원하는 바를 이룰 수 있는지 확인한다.

## 문제 이해
문제에 접근하면 Hello world가 출력되고 파일이 `hello.txt`, `index.php`, `password.php`이 있다는 것을 알 수 있다.

그리고 URL에 GET방식으로 file로써 hello가 전달되고 있음을 알 수있다.

이 문제는 password.php를 file로써 전달하여 password를 알아내는 문제임을 추측할 수 있다.

## 문제 해결 방안
GET방식으로 전달할때 hello만을 전달하는것을 보아 .txt는 코드상에서 추가된다는 것을 추측할 수 있었다.

따라서 .txt를 입력하지 않기위하여 URL 인코딩 방식으로 문자열의 끝을 알리는 null 문자를 입력하였다.

위를 이용하여 …?file=password.php%00 를 입력하자 Hello world가 출력되었던 부분에 flag가 출력되었다.

해당 flag를 auth에 입력하자 문제풀이에 성공한다.