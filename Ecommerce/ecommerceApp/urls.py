from django.urls import path
from ecommerceApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('order_complete', views.order_complete, name='order_complete'),
    path('place_order', views.place_order, name='place_order'),
    path('register', views.register, name='register'),
    path('search_result', views.search_result, name='search_result'),
    path('signin', views.signin, name='signin'),
    path('store/<str:arg>', views.store, name='store'),
    path('store', views.store, name='store'),
    path('<slug:c_slug>/<slug:p_slug>', views.product_detail, name='product_detail'),
]