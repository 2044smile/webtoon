import requests
import time
import bs4
from .models import Webtoon


def webtoon(day):
    html = requests.get("https://comic.naver.com/webtoon/weekdayList.nhn?week=" + day)

    bs_object = bs4.BeautifulSoup(html.text, "html.parser")
    webtoon_list = bs_object.find('ul', {'class': 'img_list'}) # 태그이름 , 클래스이름

    for webtoon in webtoon_list.findAll('li'): # li 태그를 다 가지고와라
        webtoon_detail = webtoon.find('dt')

        webtoon_model = Webtoon()
        webtoon_model.webtoon_id = "네이버_" + webtoon_detail.find('a')['title']
        webtoon_model.site_name = "네이버"
        webtoon_model.webtoon_name = webtoon_detail.find('a')['title']
        webtoon_model.webtoon_author = webtoon.find('dd').find('a').text
        webtoon_model.webtoon_img_url = webtoon.find('img')['src']

        webtoon_model.save()

        print(webtoon_detail.find('a')['title']) # 웹툰 이름
        print(webtoon.find('dd').find('a').text) # 작가이름
        print(webtoon.find('img')['src']) # img 의 src를 가져와라


def get_artists(artists):
    artist = ''
    for i in artists:
        artist += i.get('name') + '/'
    return artist[:-1]


def daum_webtoon(day):
    json = requests.get("http://webtoon.daum.net/data/pc/webtoon/list_serialized/" + day + "?timeStamp=" + str(int(time.time()))).json()

    for webtoon in json.get('data'):
        # print(webtoon)
        # print(webtoon.get('title')) # 웹툰이름
        # print(webtoon.get('thumbnailImage2').get('url')) # img
        # print(get_artists(webtoon.get('cartoon').get('artists'))) # 작가
        webtoon_model = Webtoon()
        webtoon_model.webtoon_id = webtoon.get('title')
        webtoon_model.site_name = "다음"
        webtoon_model.webtoon_name = webtoon.get('title')
        webtoon_model.webtoon_author = get_artists(webtoon.get('cartoon').get('artists'))
        webtoon_model.webtoon_img_url = webtoon.get('thumbnailImage2').get('url')
        webtoon_model.save()


def webtoon_all():
    week_day = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    for day in week_day:
        webtoon(day)


def daum_webtoon_all():
    week_day = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    for day in week_day:
        daum_webtoon(day)


