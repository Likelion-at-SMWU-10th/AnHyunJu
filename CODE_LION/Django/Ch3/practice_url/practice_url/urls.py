from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first),
    path('second/', views.second),

    # 다른 app에 있는 url에서 가져와서 관리..! 장고에게 나 url 따로 관리할거야! 알려주기
    path('product/', include('product.urls')),
    path('board/', include('board.urls')),
]