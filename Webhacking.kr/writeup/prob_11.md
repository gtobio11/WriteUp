# Webhacking.kr No.11

## 문제 출제 의도
정규표현식을 이해하고 있는지 확인한다.

## 문제 해석
문제에 접근하면 
$pat="/[1-3][a-f]{5}_.*IP주소.*\tp\ta\ts\ts/";

if(preg_match($pat,$_GET[val])) { echo("Password is ????"); }

가 출력되는데 해당 $pat 안의 정규표현식을 이해하여 GET 방식을 통하여 val로 전달하면 문제풀이한다.

## 문제 해결 방안
* [1-3]은 1에서 3 중의 하나 문자를 의미한다.

* [a-f]{5}는 a에서 f 중의 하나 문자를 5번 반복하라는 것을 의미한다.

* _는 _문자열 그 자체이다.

* .는 앞의 문자열이 한개의 문자만이 일치한다.

* *은 0개 이상의 문자가 일치한다.

* \t는 탭을 의미한다.

앞의 저것들을 조합하여 보면 1aaaaa_.IP주소.%09p%09a%09s%09s을 val 값으로 입력하면 콩크레츄레이션~ 이 출력되면서 문제 풀이에 성공한다.