import requests
from pprint import pprint

getdata = requests.get('http://192.168.139.131/halice/')
data = getdata.status_code == requests.codes.ok
print('Status code:')
print('------------------------------')
print(data)
if data == True:
    print('Status OK')
    print(getdata.status_code)
else:
    print('Failed')
print()
print('Headers:')
print('------------------------------')
url = 'http://192.168.139.131/halice/'
header = requests.head(url)


xheaders = {'User-Agent': 'Mobile'}
xz = requests.get(url, headers=xheaders)
for x in header.headers:
    print("\t ", x, ":", header.headers[x])
pprint(xz.text)






