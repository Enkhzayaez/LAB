from django.urls import path
from ecommerceApp import views

urlpatterns = [
    path('', views.index, name="index"),
    path('/add', views.itemAdd, name="add"),
]


