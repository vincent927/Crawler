from bs4 import BeautifulSoup
import requests

url = 'http://zhuanzhuan.58.com/detail/773468225514520580z.shtml?fullCate=5%2C38484%2C23094&fullLocal=4&from=pc&PGTID=0d305a36-0000-4f05-3df8-9b92b4bc5e5f&ClickID=1'

wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text, 'lxml')
title = soup.title.text
print(title)


