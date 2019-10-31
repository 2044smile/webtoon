from django.db import models


class Webtoon(models.Model):
    webtoon_id = models.CharField(max_length=100, primary_key=True) # 중복 된 ID는 들어오지못한다.
    site_name = models.CharField(max_length=50)
    webtoon_name = models.CharField(max_length=100)
    webtoon_author = models.CharField(max_length=100)
    webtoon_img_url = models.CharField(max_length=300)
    webtoon_url = models.CharField(max_length=100)

    def __str__(self):
        return self.webtoon_name + ' : ' + self.webtoon_author