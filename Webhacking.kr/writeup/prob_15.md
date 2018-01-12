# Webhacking.kr No.15

## 문제 출제 의도
이 문제는 출제 의도를 모르겠다.

## 문제 해석
문제를 들어가기 위한 버튼을 누르면 `Access Denied`를 출력하는 alert이 뜨고 닫으면 잠시 `password is …` 이 출력되었다가 빠른 시간내에 다시 원래 페이지로 돌아온다.

## 문제 해결 방안
잠시 뜨는 password를 auth에 입력하면 문제풀이에 성공한다. 