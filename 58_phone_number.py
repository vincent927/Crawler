from bs4 import BeautifulSoup
import requests
import pymongo

client = pymongo.MongoClient('localhost', 27017)
tongcheng = client['tongcheng']
shoujihao = tongcheng['shoujihao']


def Get_phone_number(pages):
	for n in range(1, pages+1):
		url = 'http://sz.58.com/shoujihao/pn{}'.format(str(n))
		wb_data = requests.get(url)
		soup = BeautifulSoup(wb_data.text, 'lxml')
		titles = soup.select('strong.number')
		hrefs = soup.select('a.t')
		prices = soup.select('b.price')
		for title, href, price in zip(titles, hrefs, prices):
			data = {
				'title': title.get_text(),
				'href': href.get('href'),
				'price': price.get_text()
			}
			#print(data)
			shoujihao.insert_one(data)
		print('Done!')

Get_phone_number(10)