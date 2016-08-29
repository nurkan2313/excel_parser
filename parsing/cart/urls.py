from django.conf.urls import url
from cart import views

app_name = 'cart'

urlpatterns = [
    url(r'^add_product_to_cart/(?P<product_id>[0-9]+)$', views.add_product_to_cart, name='add_product'),
]