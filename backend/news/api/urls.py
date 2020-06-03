from django.urls import path
from news.api.views import (ArticleListCreateAPIView,
                            ArticleDetailAPIView,
                            JournalistCreateAPIView)

urlpatterns = [
    # path('articles/', article_list_create_api_view, name='article_list'),
    # path('articles/<int:pk>/', article_detail_api_view, name='article_detail')
    path('articles/', ArticleListCreateAPIView.as_view(),
         name='article_list'),
    path('articles/<int:pk>/', ArticleDetailAPIView.as_view(),
         name='article_detail'),
    path('journalists/', JournalistCreateAPIView.as_view(),
         name='journalist_list'),
]
