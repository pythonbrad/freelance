from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('signin', views.signin, name='signin'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('about', views.about, name='about'),
    path('details/<int:pk>', views.details, name='details'),
    path('become-seller/<int:pk>', views.become_seller, name='become_seller'),
    path('<str:tag>', views.index, name='home'),
]
