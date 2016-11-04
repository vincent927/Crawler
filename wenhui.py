from bs4 import BeautifulSoup
import requests
from datetime import *









def Get_urls():
	urls = []
	dt = datetime.now()
	today = (str(dt.strftime('%Y%m%d')))
	url = 'http://news.wenweipo.com/list_srh.php?date={}&cat=000IN&instantCat=finance'.format(today)
	wb_data = requests.get(url)
	soup = BeautifulSoup(wb_data.content, 'lxml')
	hrefs = soup.select('a.sub_fg16')
	for href in hrefs:
		href = href.get('href')
		urls.append(href)
#	print(urls)
	return urls





def Get_info():
	urls = Get_urls()
	for url in urls:
		wb_data = requests.get(url)
		soup =  BeautifulSoup(wb_data.content, 'lxml')
		title = soup.select('h1.title')
		author = soup.select('p.fromInfo')
		time = soup.select('span.date')
		source = soup.select('span.current')
		a = soup.select('#main-content p')
		print(title,author,time,source)


Get_info()