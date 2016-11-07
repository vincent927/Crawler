from bs4 import BeautifulSoup
from datetime import *
import requests
import pymongo

dt = datetime.now()
today = (str(dt.strftime('%Y%m%d')))


client = pymongo.MongoClient('localhost', 27017)
wenhui = client['wenhui']
finance = wenhui['finance']

finance_url = 'http://news.wenweipo.com/list_srh.php?date=20161104&cat=000IN&instantCat=finance'

headers = {
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Encoding':'gzip, deflate, sdch',
	'Accept-Language':'zh-CN,zh;q=0.8',
	'Cache-Control':'no-cache',
	'Connection':'keep-alive',
	'Host':'news.wenweipo.com',
	'Pragma':'no-cache',
	'Referer':'http://news.wenweipo.com/list_srh.php?date=20161104&cat=000IN&instantCat=finance',
	'Upgrade-Insecure-Requests':'1',
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
	}









def Get_urls():
	urls = []
	dt = datetime.now()
	today = (str(dt.strftime('%Y%m%d')))
	today = '20161104'
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
		wb_data = requests.get(url, headers=headers)
		soup =  BeautifulSoup(wb_data.content, 'lxml')
		titles = soup.select('h1.title')
		authors = soup.select('p.fromInfo')
		dates = soup.select('span.date')
		sources = soup.select('span.current')
		times = Get_time(finance_url)
		texts = soup.select('body')
		for title, author, date, source, time, text in zip(titles, authors, dates, sources, times, texts):
			data = {
				'title': title.get_text(),
				'author': author.get_text()[5:],
				'date': date.get_text(),
				'source': source.get_text(),
				'url': url,
				'time': time.get_text()[6:-2],
				'text': text.get_text()
			}
#			print(data['text'])
#			finance.insert_one(data)


def Get_time(url):
	wb_data = requests.get(url)
	soup = BeautifulSoup(wb_data.content,'lxml')
	times = soup.select('span.date')
	return times

Get_info()