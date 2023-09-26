from django.contrib import admin
from django.urls import path, include
from ecommerceApp import urls as e_urls

urlpatterns = [
    path('', include(e_urls)),
    path('admin/', admin.site.urls),
]


