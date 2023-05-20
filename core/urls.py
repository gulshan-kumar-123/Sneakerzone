from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('',views.index, name='index'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('cart/', views.cart, name='cart'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('search/', views.search, name='search'),
    path('browse/', views.browse, name='browse'),
]