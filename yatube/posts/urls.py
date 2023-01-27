# posts/urls.py
from django.urls import path
from . import views


app_name = 'posts'
urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    # Страницы с отфильтрованными по группам постами
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
]
