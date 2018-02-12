# Wargame.kr No.01 - already_got

## 문제 출제 의도
HTTP 헤더를 읽을 수 있는지 확인한다.

## 문제 이해
문제에 접근하기 전에 힌트로 `can you see HTTP Response header?`가 출력된다.

문제에 접근하여 flag를 찾으면 되는 문제인데 문제에 접근하면

`you've already got key! :p`가 출력된다.

힌트를 보아 HTTP 통신 중 Response header를 읽을 줄 안다면 해결되는 문제인 것 같다.

## 해결 방안
Chrome을 접근하여 개발자 도구를 열어보게 되면 Network에서 편하게 Response header를 확인할 수 있다.

Response header를 보면 떡하니 flag가 출력된다.

해당 flag를 auth에 입력하면 문제 풀이에 성공한다.