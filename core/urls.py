from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('signin', views.signin, name='signin'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('about', views.about, name='about'),
    path('details/<int:pk>', views.details, name='details'),
    path('become-seller', views.become_seller, name='become_seller'),
    path('seller-account', views.seller_account, name='seller_account'),
    path('buyer-account', views.buyer_account, name='buyer_account'),
    path('<str:tag>', views.index, name='home'),
]
