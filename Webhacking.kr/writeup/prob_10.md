# Webhacking.kr No.10

## 문제 출제 의도
코드를 분석하여 원하는 바에 쉽게 접근하는 방법을 안다.

## 문제 해석
문제에 접근하여 코드를 분석해볼 시에 a 링크에 마우스 클릭 이벤트와 hover 이벤트가 걸려있었다.

클릭 이벤트에는 클릭시마다 this.style.posLeft를 1씩 증가시키고 800 일때에 URL에 go=this.style.posLeft 값을 입력한다.

this.style.posLeft가 증가할때마다 O가 오른쪽으로 이동한다.

호버 이벤트에는 O를 yOu로 바꾸어 보여준다.

## 문제 해결 방안
버튼을 800번 클릭하면 콩크레츄레이션~ 이 출력되면서 문제 풀이에 성공하는데 너무 힘들다.

따라서 개발자 도구에 들어가 1씩 증가하는 값을 800으로 바꾸어 주면 단 한번의 클릭으로 문제 풀이에 성공한다.