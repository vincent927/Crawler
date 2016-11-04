from bs4 import BeautifulSoup
import requests


def Get_phone_number():
	for n in range(1, 100):
		url = 'http://sz.58.com/shoujihao/pn{}'.format(str(n))
		wb_data = requests.get(url)
		soup = BeautifulSoup(wb_data.text,'lxml')
		titles = soup.select('strong.number')
		hrefs = soup.select('a.t')
		for title, href in zip(titles,hrefs):
			data = {
				'title': title.get_text(),
				'href': hrefs.get('a.href')
			}
			print(data)
Get_phone_number()