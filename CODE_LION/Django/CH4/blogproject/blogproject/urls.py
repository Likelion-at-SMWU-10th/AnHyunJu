from unicodedata import name
from django.contrib import admin
from django.urls import path
from blogapp import views

from django.conf import settings
from django.conf.urls.static import static

from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),

    # html form을 이용해서 블로그 객체 만들기
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),

    #django form을 이용해서 블로그 객체 만들기
    path('formcreate/', views.formcreate, name="formcreate"),

    #django modelform을 이용해 블로그 객체 만들기
    path('modelformcreate/', views.modelformcreate, name="modelformcreate"),

    #127.0.0.1:8000/datil/1 이런식으로 페이지를 만들고 싶다
    path('detail/<int:blog_id> ',  views.detail, name='detail'),

    #댓글 저장 url
    path('create_comment/<int:blog_id> ',  views.create_comment, name='create_comment'),

    #login path 등록
    path('login/',  accounts_views.login, name='login'),
     path('logout/', accounts_views.logout, name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# media 파일에 접근할 수 있는 url도 추가해줘야함(위의 형태와 아래의 형태가 같음)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)