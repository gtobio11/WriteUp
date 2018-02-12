# Wargame.kr No.03 - free_button

## 문제 출제 의도
웹 코드를 읽고 목적이 다가가는 방법을 안다.

## 문제 이해
문제에 접근하기 전 힌트에 `click the button!     i can't catch it!`이 출력된다.

문제에 접근하게 되면 `click button, if you want to get the authentication key`가 출력되며 버튼이 마우스를 쫓아다닌다.

버튼을 클릭하면 문제가 해결되는 것 같다.

## 문제 해결 방안
개발자도구를 통하여 코드를 읽어보면 div태그안에 input요소 type 속성이 button인 태그가 있는데 onclick 함수에 `window.location="?key=b69b"`인것을 보아 url에 GET방식으로 `?key=b69b`를 입력해 보니 flag가 출력되었고 해당 flag를 auth에 입력하니 문제풀이에 성공한다.