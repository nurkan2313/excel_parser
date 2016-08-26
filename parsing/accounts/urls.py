from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^new_acc/$', views.signup, name='new_acc'),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^signout/$', views.signout, name='signout'),
]