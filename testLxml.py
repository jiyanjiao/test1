import requests
from bs4 import BeautifulSoup

response = requests.get('http://www.gov.cn/pushinfo/v150203/index.htm')
soup = BeautifulSoup(response.text,features='lxml')
for link in soup.find_all(name="a"):
       if 'href' in  link.attrs:
           print(link.attrs['href'])
