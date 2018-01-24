# Webhacking.kr No.34

## 문제 출제 의도
자바 스크립트 코드를 읽어 출제자가 원하는 입력을 실행할 수 있는지 확인한다.

## 문제 이해
문제에 접근하면 `Wrong`이라는 내용을 담은 경고 창이 출력된다.

문제에 들어가 개발자 도구를 확인하면 난독화 되어있는 JS 코드가 출력된다.

난독화 되어있는 코드 최 하단부에 `if(document.URL.indexOf('0lDz0mBi2')!=-1){location.href='Passw0RRdd.pww';}else{alert('Wrong');}`이러한 코드가 출력된다.

## 문제 해결 방안
`if(document.URL.indexOf('0lDz0mBi2')!=-1){location.href='Passw0RRdd.pww';}else{alert('Wrong');}` 이 코드 안에 있는 location.href='passw0RRdd.pww'를 보아 passw0RRdd.pww에 접근해보아야 할것 같다. 

`http://webhacking.kr/challenge/javascript/Passw0RRdd.pww`과 같이 passw0RRdd.pww 에 접근하여 보면 flag가 출력된다.

해당 flag를 Auth에 입력하면 문제 풀이에 성공한다.