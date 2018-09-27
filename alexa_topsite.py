import requests
import re

url = 'https://www.alexa.com/topsites/countries/IN'
head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
html = requests.get(url,headers = head).text
site = re.findall(r'<a href="/siteinfo/(.*?)">',html,re.S)
f =open('in_top50_site.txt','w',encoding = 'utf-8')
for i in site:
    f.write(i+'\n')