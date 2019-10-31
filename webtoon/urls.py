from django.urls import path
from .views import *


urlpatterns = [
    path('', WebtoonList.as_view(), name='list'),
    path('naver_webtoon/', naver_webtoon, name='naver_webtoon'),
    path('daum_webtoon/', daum_webtoon, name='daum_webtoon'),
    path('naver/', NaverList.as_view(), name='naver'),
    path('daum/', DaumList.as_view(), name='daum'),
]