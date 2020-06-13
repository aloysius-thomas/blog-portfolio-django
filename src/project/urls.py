from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path

from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('user/', include('accounts.urls')),
    path('blog/', include('blog.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path('admin/', admin.site.urls),
    ]
