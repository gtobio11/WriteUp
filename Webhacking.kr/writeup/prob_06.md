# Webhacking.kr No.06

## 문제 출제 의도
php 코드를 이해하고 base_64 방식으로 원하는 문자열을 암호화 시킬 수 있는지 확인한다.

## 문제 해석
문제에 들어가 index.phps에 들어가 소스코드를 읽어보면 기본으로 설정되어있는 id값과 pw값을 base_64방식으로 20번 암호화 한후에 특정 문자를 치환시킨다.

그리고 치환까지 마친 문자열을 쿠키의 값에 저장시킨후에 해당 쿠키에 저장된 문자열을 치환된 값을 원래대로 돌리고 다시 20번 복호화를 거친후에 출력시켜준다.

## 문제 해결 방안
admin 문자를 base_64방식으로 20번 암호화하고 치환해야하는 문자열이 있을 경우 치환시켜 나온 값을 쿠키에 저장시켜주면 문제 풀이에 해결한다.