
from django.contrib import admin
from django.urls import path, include
from ecommerceApp import urls as e_urls
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include(e_urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)