from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_admin'),
    path('contact/', views.contact, name='contact_admin'),
    path('messages/', views.messages, name='messages'),
    path('authors/', views.authors, name='authors'),
    path('post/', views.post, name='post')
]