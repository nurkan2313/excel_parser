from django.conf.urls import url
from profiles import views

urlpatterns = [
    url(r'^profile/$', views.profile_detail_private, name='profile_detail_private'),
]