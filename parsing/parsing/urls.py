from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from . import settings
from linkparser import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^parser/', include('linkparser.urls', namespace='parser')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +\
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)