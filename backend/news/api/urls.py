from django.urls import path
from news.api.views import (ArticleListCreateAPIView,
                            ArticleDetailAPIView,
                            JournalistCreateAPIView,
                            BookListCreateAPIView,
                            BookDetailAPIView,
                            ReviewListCreateAPIView,
                            ReviewDetailAPIView)

urlpatterns = [
    # path('articles/', article_list_create_api_view, name='article_list'),
    # path('articles/<int:pk>/', article_detail_api_view, name='article_detail')
    path('articles/', ArticleListCreateAPIView.as_view(),
         name='article_list'),
    path('articles/<int:pk>/', ArticleDetailAPIView.as_view(),
         name='article_detail'),
    path('journalists/', JournalistCreateAPIView.as_view(),
         name='journalist_list'),
    path('books/', BookListCreateAPIView.as_view(),
         name='book_list'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(),
         name='book_detail'),
    path('books/<int:pk>/review/', ReviewListCreateAPIView.as_view(),
         name='review_list'),
    path('reviews/<int:pk>/', ReviewDetailAPIView.as_view(),
         name='review_detail'),
]
