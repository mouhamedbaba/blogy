from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:post_id>' , views.single, name='single'),
    path('blog/', views.blog, name='blog'),
    path('categorie/<str:cat_name>', views.categorie, name='categorie'),
    path('search/', views.search, name='search'),
    path('contact/', views.contact, name='contact')
]
