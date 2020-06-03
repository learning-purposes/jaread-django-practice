from django.urls import path
<<<<<<< HEAD
from .views import article_list_create_api_view

urlpatterns = [
    path('articles/', article_list_create_api_view, name='article_list'),
=======

from news.api.views import article_list_create_api_view, article_detail_api_view

urlpatterns = [
    path('articles/', article_list_create_api_view, name='article_list'),
    path('articles/<int:pk>/', article_detail_api_view, name='article_detail')
>>>>>>> 9779852ed0153235eaf3b3b2c7ee3f9395cf95f7
]
