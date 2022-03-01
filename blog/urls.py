from django.urls import path

from .views import home, article_detail

app_name = 'blog'

urlpatterns = [
    path('', home, name='home'),
    path('<str:slug>/', article_detail, name='article_detail'),
]