# webhacking.kr No.21

## 문제 출제 의도
DB의 구조를 이해하고 Blind SQL Injection 할 수 있는지 확인한다.

## 문제 해석
문제에 접근하여 출력된 화면을 보면 input 태그와 제출 버튼이 있다.

그 하단에 Result: False가 출력된다.

소스코드를 읽어보면 form 태그 안에 no와 id, pw를 넣어 보낸다는 것을 알 수 있었다.

## 문제 해결 방안
우선 DB의 구조를 이해해보기 위해서 no값에 1부터 순서대로 입력해보았다.

no가 2일때까지는 True를 출력해주지만 3 이상일때에는 False를 출력함을 보아 DB는 no가 2일때까지만 존재한다는 것을 알 수 있었다.

아마 DB의 크기가 2개인것을 보아 `guest`와 `admin`으로 구성되어있을것이라고 추측할 수 있었다.

no의 값으로 조작하면서 admin과 guest의 no값을 구분하여보았다.

우선 no=1 and ascii(substr(id,1,1)) = 97 로 no가 1일때의 id값이 `admin`인지 확인해보았으나 False가 출력되어 no=2 and ascii(substr(id,1,1)) = 97을 입력해 보았더니 True가 출력되었다.

혹시 모를 경우를 대비하여 no=2 and ascii(substr(id,2,1)) = 100을 해보았더니 역시 True가 출력됨을 보아 no가 2일때 `admin`임을 확인하였다.

pw값을 알아보아야 하는데 pw의 길이를 알기위하여 no=2 and ascii(substr(id,1,1)) = 97 and length(pw)>8 이와같이 대충 추려내보았더니 no=2 and ascii(substr(id,1,1))=97 and length(pw)=19 일때 True가 출력되면서 admin의 pw 길이가 19 임을 알 수 있었다.

길이가 19인 문자열을 손으로 구하기는 어려우므로 파이썬 코드로 코딩해보았다. 해당 코드는 `../src/prob_21.py`이다.