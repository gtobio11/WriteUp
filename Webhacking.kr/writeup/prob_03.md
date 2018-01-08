# Webhacking.kr No.03

## 문제 출제 의도
웹 페이지가 의미하는 바를 이해하고 SQL Injection을 수행할 수 있는지 확인한다.

## 문제 이해
처음 문제를 열어보면 이상한 페이지를 출력하는데 네모로직임을 알 수 있었다. 해당 네모로직을 해결하고 gogo버튼을 누르면 다음 페이지로 이동한다.

name을 입력하는 창에 아무 값이나 입력하고 http 소켓을 열어보니 id 값에 입력한 값이 answer에 1010…1111 과 같은 값이 들어있음을 알 수 있다.

## 문제 해결 방안
name을 입력하는 창이 id를 의미하는 만큼 admin입력하고 answer 값을 조작해볼수 있었다. 

필자는 크롬을 사용하여 문제를 해결하였는데 크롬 개발자 도구를 열어 1010…1111과 같은 값이 들어있는 input 태그가 있는 것을 볼 수 있었는데 이 값을 || 연산으로 조작하여 항상 참이 되도록 해보았더니 페이지가 이동하면서 answer값에 flag가 출력되었다.

해당 flag를 Auth에 입력하면 문제 풀이에 성공한다.