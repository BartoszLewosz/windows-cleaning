from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, {'pagename': ''}, name='home'),
    path('contact', views.contact, name='contact'),
    path('privacy', views.privacy, name='privacy'),
    path('<str:pagename>', views.index, name='index'),
]
