from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Core.views import singup, profile, singin, singout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('singup/', singup, name='singup'),
    path('profile/', profile, name='profile'),
    path('singin/', singin, name='singin'),
    path('singout/', singout, name='singout')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
