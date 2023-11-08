from django.urls import path
from cartssApp import views

urlpatterns = [
    path('', views.index, name='cartss'),
    path('add_cartss/<int:product_id>/', views.add_cart, name='add_cartss'),
    path('remove_cartss/<int:product_id>/', views.remove_cart, name='remove_cartss'),
    path('remove_cartss_item/<int:product_id>/', views.remove_cartItem, name='remove_cartssItem')
]