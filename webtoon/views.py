from django.shortcuts import render
from django.http import HttpResponse
from webtoon.naver_webtoon import webtoon_all, daum_webtoon_all
from django.views.generic import ListView
from .models import *


class WebtoonList(ListView):
    model = Webtoon
    paginate_by = 40


def naver_webtoon(request):
    webtoon_all()
    return HttpResponse('네이버 웹툰 크롤링 완료')


def daum_webtoon(request):
    daum_webtoon_all()
    return HttpResponse('다음 웹툰 크롤링 완료')


class NaverList(ListView):
    model = Webtoon
    queryset = Webtoon.objects.filter(site_name='네이버')
    paginate_by = 40


class DaumList(ListView):
    model = Webtoon
    queryset = Webtoon.objects.filter(site_name='다음')
    paginate_by = 40


def search(request):
    ss = Webtoon.objects.all() # 웹툰 모든 DB
    s = request.GET.get('s', '') #
    if s:
      ss = ss.filter(webtoon_name__icontains=s)

    return render(request, 'webtoon/webtoon_list.html', {
        'ss': ss,
        's': s,
    })
