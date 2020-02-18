from django.urls import path

from articles.views import ArticleViewSet, toggle_like

article_list = ArticleViewSet.as_view({
    'get': 'list'})
article_detail = ArticleViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('articles/', article_list, name='article-list'),
    path('articles/<int:pk>/', article_detail, name='article-detail'),
    path('articles/toggle_like/<int:pk>/', toggle_like, name='article-toggle-like'),
]
