from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.pagination_pars_page, name='pars_page')
]