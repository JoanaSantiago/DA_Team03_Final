import requests

getdata = requests.get('http://172.18.58.238/halice/')
data = getdata.status_code == requests.codes.ok
if data == True:
    print('Status OK')
    print(getdata.status_code)
else:
    print('Failed')
xheaders = {'User-Agent': 'Mobile'}
xz = requests.get(headers=xheaders, url='http://172.18.58.238/halice/')
print(xz.headers)
