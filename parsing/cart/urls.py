from django.conf.urls import url
from cart import views


urlpatterns = [
    url(r'^add_product_to_cart/(?P<product_id>[0-9]+)$', views.add_product_to_cart, name='add_product'),
    url(r'^cart_list/$', views.cart_list, name='cart_list'),
]