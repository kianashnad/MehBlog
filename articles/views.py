from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from articles.models import Article
from articles.serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def toggle_like(request, article_id):
    from django.shortcuts import get_object_or_404
    from articles.models import Like
    from rest_framework.response import Response

    article = get_object_or_404(Article, pk=article_id)
    liked = Like.objects.filter(sender=request.user, article=article)

    if len(liked) == 0:
        article.amount_like += 1
        Like(sender=request.user, article=article).save()
        return Response({"message": "success"}, status=200)

    else:
        article.amount_like -= 1
        liked[0].delete()
        return Response({"message": "success"}, status=200)
