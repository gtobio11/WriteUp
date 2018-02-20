# Wargame.kr No.13 - tmitter

## 문제 출제 의도
php의 trim함수와 Database의 특징을 이용하여 문제를 풀수있는지 확인한다.

## 문제 이해
문제에 접근하기 전에 Database 테이블에 대한 설명을 힌트로 제공한다. id, pw가 32자 제한으로 이루어져 있다고 알려준다.

문제에 접근하면 sign up과 sign in 이 출력되면서 회원가입과 로그인을 할 수 있는 화면이 출력된다.

회원가입 란의 input태그는 maxheight로 32자를 제한하고 있고 최저 글자수또한 제한하고 있는것 같았다.

admin으로 회원가입을 시도했지만 이미 있다며 되지 않았다.

## 문제 해결 방안
아마 회원가입할때 id에 앞뒤 공백을 지우기 위하여 trim함수를 사용할 것 이라고 추측하였고 database의 특징과 연계하여 문제를 접근하였다.

database는 최대 글자수를 제한을 두는데 이 database에서는 32자로 제한하고 있었다.

이때 32자 이상을 입력하게 되면 32자 이후의 글자는 모두 삭제하고 접근한다.

여기서 trim을 사용하게 되면 공백을 모두 지워주며 database에 입력한다.

이것을 이용하여 admin으로 중복 회원가입을 시도하였다.

`admin                           1`과 같이 admin과 공백을 포함하여 32자를 채운후 그 뒤에 아무 글자를 입력하게되면 필터링을 통과하고 1이 삭제되어 database에서 trim함수로 공백을 제거하여 새로운 열이 생성되는것을 이용하였다.

위의 방법으로 회원가입한 것으로 로그인을 하면 flag가 출력되고 해당 flag를 auth에 입력하며 문제풀이에 성공한다.