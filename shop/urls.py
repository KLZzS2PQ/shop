from django.core.handlers.wsgi import WSGIRequest
from django.urls import path
from .views import catalog, order_create, orders, product_info

urlpatterns = [
    path('catalog/', catalog, name='catalog'),
    path('order_create/<int:id>/', order_create, name='order_create'),
    path('orders/', orders, name='orders'),
    path('product_info/<int:id>/', product_info, name='product_info'),
]
