import requests
from bs4 import BeautifulSoup

url  = "http://top100.nchu.edu.tw/nchubody2.php"
res  = requests.get(url)

list = ['排名：', '單位：', 'IP：', '上傳：', '下載：', '總流量：']

n = 0
soup = BeautifulSoup(res.text, 'html.parser')
for font in soup.select('[color="red"]'):
	print( list[n] + font.get_text() )
	n = n+1