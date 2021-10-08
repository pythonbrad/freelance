from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
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
    path('create-microservice', views.create_microservice, name='create_microservice'),
    path('<str:tag>', views.index, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) if settings.DEBUG else []
