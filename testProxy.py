import requests

#设置代理网址:http://www.xicidaili.com/

proxy1 = {'http':'111.155.116.245:8123','https':'101.132.122.230:3128'}
response = requests.get('https://www.baidu.com',proxies = proxy1)
print(response.content.decode('utf-8'))