from django.urls import path
from board import views

urlpatterns = [
    path('', views.boardlist), # 기본 board/ 일 경우 
    path('first/', views.boardfirst),  #board/first/
]