from bs4 import BeautifulSoup
import requests




def GetUrl(page=3):
	urls = []
	for i in range(1, page + 1):
		url='http://sz.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(page))
		urls.append(url)
	print(urls)


GetUrl()








