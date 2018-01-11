# Webhacking.kr No.11

## 문제 출제 의도
javascript를 개발자도구 console창을 이용하여 조작할 수 있는지 확인한다.

## 문제 해석
문제에 접근하면 화면에 javascript challenge라는 문구가 출력된다.

해당 문구를 본 후에 개발자도구를 열어 소스보기를 하면 script태그 안에 난독화 되어있는 아스키코드들이 나열되어있고 그 아스키코드들을 문자로 바꾸어주는 String.fromCharCode()함수를 이용한 리턴값을 WorkTimeFun 변수에 저장한다.

## 문제 해결 방안
WorkTimeFun 변수에 담긴 문자열을 보기 위해서 개발자도구의 console창에 console.log(WorkTimeFun)과 같은 출력시킬 수 있는 방안을 사용하면 
```javascript
var enco='';
var enco2=126;
var enco3=33;
var ck=document.URL.substr(document.URL.indexOf('='));
 
 
for(i=1;i<122;i++)
{
enco=enco+String.fromCharCode(i,0);
}
 
function enco_(x)
{
return enco.charCodeAt(x);
}
 
if(ck=="="+String.fromCharCode(enco_(240))+String.fromCharCode(enco_(220))+String.fromCharCode(enco_(232))+String.fromCharCode(enco_(192))+String.fromCharCode(enco_(226))+String.fromCharCode(enco_(200))+String.fromCharCode(enco_(204))+String.fromCharCode(enco_(222-2))+String.fromCharCode(enco_(198))+"~~~~~~"+String.fromCharCode(enco2)+String.fromCharCode(enco3))
{
alert("Password is "+ck.replace("=",""));
}
```
가 출력된다
해당 코드를 분석하여 보면 if문안에서 ck가 어떠한 문자열일때 ck에서 = 를 지운 값이 flag가 된다는 것을 알 수 있다. 따라서 if문의 ck==을 제외한 비교문을 복사하여 console창에 입력한다면 flag가 나오며 그 flag를 Auth에 입력하면 문제 풀이에 성공한다.

