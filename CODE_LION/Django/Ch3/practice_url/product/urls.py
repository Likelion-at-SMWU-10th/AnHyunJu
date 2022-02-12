from django.urls import path
from product import views

urlpatterns = [
    path('', views.productlist), # 기본 product/ 일 경우 
    path('first/', views.productfirst),  #product/first/
]