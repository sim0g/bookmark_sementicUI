from django.db import models

# Create your models here.
# 사이트 이름과 URL이 필요해요.
class Bookmark(models.Model):
    site_name =  models.CharField(max_length=200)
    url = models.URLField('Site URL')
    def __str__(self):
        return self.site_name + " ▶  " + str(self.url)
# admin 파일이 이걸 인식할수 있도록 해줘야해요.

