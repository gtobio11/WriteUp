# Webhacking.kr No.20

## 문제 출제 의도
문제가 원하는바를 알고 그에 빠르게 접근하기 위하여 javascript console을 이용할 줄 아는지 확인한다.

## 문제 해석
```html
<form name=lv5frm method=post>
<table border=0>
<tr><td>nickname</td><td><input type=text name=id size=10 maxlength=10></td></tr>
<tr><td>comment</td><td><input type=text name=cmt size=50 maxlength=50></td></tr>
<tr><td>code</td><td><input type=text name=hack><input type=button name=attackme value="iigcbbbdmi"
 style=border:0;background=lightgreen onmouseover=this.style.font=size=30 onmouseout=this.style.font=size=15></td></tr>
<tr><td><input type=button value="Submit" onclick=ck()></td><td><input type=reset></td></tr>
</table>
<script>
function ck()
{

if(lv5frm.id.value=="") { lv5frm.id.focus(); return; }
if(lv5frm.cmt.value=="") { lv5frm.cmt.focus(); return; }
if(lv5frm.hack.value=="") { lv5frm.hack.focus(); return; }
if(lv5frm.hack.value!=lv5frm.attackme.value) { lv5frm.hack.focus(); return; }

lv5frm.submit();

}
</script>
```
* 입력된 id값이 비어있지 않을때 id에 focus() 함수를 실행시키고 return한다.

* 입력된 cmt값이 비어있지 않을때 cmt에 focus() 함수를 실행시키고 return한다.

* 입력된 hack값이 비어있지 않을때 hack에 focus() 함수를 실행시키고 return한다.

* 입력된 hack의 값이 attackme의 값과 다를때 hack에 focus() 함수를 실행시키고 return한다.
## 문제 해결 방안
id, comment를 입력하고 attackme의 값을 hack에 입력하고 submit을 하는데 wrong이 출력된다.

이유는 timeslice가 2 이기 때문인데 위의 저것들을 입력하는데 wrong이 출력되는것을 보아 2초 인것을 알 수 있다.

이를 극복하기 위하여 javascript console을 이용할 것이다.

lv5frm.id.value="gtobio11"; // gtobio11는 제 닉네임입니다.
lv5frm.cmt.value="2초는좀아니지 그쵸?";
lv5frm.hack.value=lv5frm.attackme.value;
ck()

를 복사하고 개발자도구의 console창에 붙여넣기하여 값을 채운후 ck함수를 불러온다면 문제풀이에 해결한다. 코드의 난이도는 낮기때문에 자세한 설명은 생략한다.