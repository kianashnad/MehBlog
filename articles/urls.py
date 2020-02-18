from django.urls import path

from articles.views import ArticleViewSet

article_list = ArticleViewSet.as_view({
    'get': 'list'})
article_detail = ArticleViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('articles/', article_list, name='article-list'),
    path('articles/<int:pk>/', article_detail, name='article-detail'),
]
