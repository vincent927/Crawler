from multiprocessing import Pool
from channel_extact  import channel_list
from pages_parsing   import get_links_from
from pages_paring import get_item_info
import pymongo

client = pymongo.MongoClient('localhost', 27017)
ceshi = client['ceshi']
url_list4 = ceshi['url_list4']


def get_all_links_from(channel):
    for i in range(1,100):
        get_links_from(channel,i)


if __name__ == '__main__':
    pool = Pool()
    # pool = Pool(processes=6)
    pool.map(get_all_links_from,channel_list.split())
    pool.map()
    url_list4.find()


