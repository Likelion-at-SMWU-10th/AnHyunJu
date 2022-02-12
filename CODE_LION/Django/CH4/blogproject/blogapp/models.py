from tokenize import blank_re
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200) # 글자수 제한
    body = models.TextField()
    photo = models.ImageField(blank=True, null=True, upload_to='blog_photo')
    date = models.DateTimeField(auto_now_add=True) # 자동으로 지금시간 추가

    #admin 사이트에서 보이는 제목을 글의 제목으로 설정하는 코드
    def __str__(self):
        return self.title


#댓글달기
class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True) # 자동으로 지금시간 추가
    #어떤 게시글의 댓글인지, 블로그 객체를 참조 해야한다
    #post담길 데이터는 blog객체와 관련된 것들을 넣어줘야한다. blog객체를 참조하는 foreign Key
    post = models.ForeignKey(Blog, on_delete=models.CASCADE) #어떤 게시글이 삭제되면 댓글도 같이 삭제 

    #admin 사이트에서 보이는 제목을 글의 제목으로 설정하는 코드
    def __str__(self):
        return self.comment