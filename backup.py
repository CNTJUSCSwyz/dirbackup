import requests
import sys
url = 'http://172.21.224.1:8888/'
import threading
a = ['bak','zip','rar','tar.gz','txt']
b = ['swp','swo','swn']
c = ['index.php', 'flag.php', 'robots','upload.php','answer.php']
s = requests.session()
proxies = {
    'http':None,
    'https':None
}
headers = {"Cookie": "PHPSESSID=sclfgjri76captre7cvq6g4170","Accept": "text/html,application/xhtml+xml,application/xml;", "Accept-Encoding": "gzip", "Accept-Language": "zh-CN,zh;q=0.8",
           "Referer": "http://www.example.com/", "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"}
for i in c:
    nurl = url +i+ '~'
    r = s.get(nurl,proxies=proxies)
    if str(r) != '<Response [404]>':
        print nurl
        sys.stdout.flush()
    for j in range(0,len(a)):
        nurl = url + i +'.'+ a[j]
        r = s.get(nurl, proxies=proxies)
        if str(r) != '<Response [404]>':
            print nurl
            sys.stdout.flush()
    for j in range(0, len(b)):
        nurl = url + '.'+ i +'.'+ b[j]
        r = s.get(nurl, proxies=proxies)
        if str(r) != '<Response [404]>':
            print nurl
            sys.stdout.flush()
print 'finish'
