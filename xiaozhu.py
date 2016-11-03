from bs4 import BeautifulSoup
import requests
import pymongo

client = pymongo.MongoClient('localhost', 27017)
xiaozhu = client['xiaozhu']
prices_tab = xiaozhu ['prices']

def GetUrl(page=3):
	urls = []
	for i in range(1, page + 1):
		url='http://sz.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(i))
		urls.append(url)
	return urls

def GetPrices():
	url_list = GetUrl()
	for url in url_list:
		wb_data = requests.get(url)
		soup = BeautifulSoup(wb_data.text, 'lxml')
		prices = soup.select('span.result_price i')
		titles = soup.select('span.result_title')
		for price, title in zip(prices, titles):
			data = {
				'price': int(price.get_text()),
				'title': title.get_text()
			}
			prices_tab.insert_one(data)


GetPrices()






