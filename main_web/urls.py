from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('build/', views.build, name='build'),
    path('shop/', views.shop, name='shop'),
    path('detail/', views.detail, name='detail'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]
