from django.urls import path
from cartApp import views

urlpatterns = [
    path('', views.index, name='cart'),
]