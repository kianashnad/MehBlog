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
def toggle_like(request, pk):
    from django.shortcuts import get_object_or_404
    from articles.models import Like
    from rest_framework.response import Response

    article = get_object_or_404(Article, pk=pk)
    liked = Like.objects.filter(article=article, sender=request.user).first()

    if liked is None:
        article.amount_like += 1
        article.save()
        Like(sender=request.user, article=article).save()
        return Response({"message": "success"}, status=200)

    else:
        article.amount_like -= 1
        article.save()
        liked.delete()
        return Response({"message": "success"}, status=200)
