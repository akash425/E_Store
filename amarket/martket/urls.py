from django.urls import path
from . import views

urlpatterns =  [
    path('',views.p_list, name = 'products'),
    path('cart/<str:pid>',views.cart, name = 'cart'),
]