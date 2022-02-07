from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200) # 글자수 제한
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True) # 자동으로 지금시간 추가

    #admin 사이트에서 보이는 제목을 글의 제목으로 설정하는 코드
    def __str__(self):
        return self.title