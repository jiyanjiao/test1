import requests
import re
url = 'https://movie.douban.com/top250'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}
response = requests.get(url,headers = headers)
print('影片排名:',re.findall(re.compile(r'<em class="">(.*)</em>'),response.text))
print('影片排名个数:',len(re.findall(re.compile(r'<em class="">(.*)</em>'),response.text)))

print('影片名字:',re.findall(re.compile('<span class="title">(.*)</span>.*?'),response.text))
print('影片名字个数:',len(re.findall(re.compile(r'<span class="title">(.*)</span>'),response.text)))

print("影片连接:",re.findall(re.compile(r'<a href="(.*)" class=""'),response.text))
print('影片连接个数:',len(re.findall(re.compile(r'<a href="(.*)" class=""'),response.text)))

print('导演:',re.findall(re.compile(r'导演: (.*)&nbsp;&nbsp;&nbsp;'),response.text))
print('导演个数:',len(re.findall(re.compile(r'导演: (.*)&nbsp;&nbsp;&nbsp;'),response.text)))

print('主演:',re.findall(re.compile(r'主演: (.*)<br>'),response.text))
print('主要个数',len(re.findall(re.compile(r'主演: (.*)<br>'),response.text)))

print('上映日期:',re.findall(re.compile(r'(\d\d\d\d)&nbsp;/&nbsp;'),response.text))
print('上映时间个数',len(re.findall(re.compile(r'(\d\d\d\d)&nbsp;/&nbsp;'),response.text)))

print('国家:',re.findall(re.compile(r'&nbsp;/&nbsp;(.*)&nbsp;/&nbsp;'),response.text))
print('国家个数:',len(re.findall(re.compile(r'&nbsp;/&nbsp;(.*)&nbsp;/&nbsp;'),response.text)))

print('剧情',re.findall(re.compile(r'&nbsp;/&nbsp;剧情 (.*)'),response.text))
print('剧情个数:',len(re.findall(re.compile(r'&nbsp;/&nbsp;剧情 (.*)'),response.text)))

print('评分',re.findall(re.compile(r'<span class="rating_num" property="v:average">(.*)</span>'),response.text))
print('评分个数:',len(re.findall(re.compile(r'<span class="rating_num" property="v:average">(.*)</span>'),response.text)))

print('评价人数',re.findall(re.compile(r'<span>(.*)人评价'),response.text))
print('评价人数个数',len(re.findall(re.compile(r'<span>(.*)人评价'),response.text)))
