from rest_framework.generics import ListAPIView, RetrieveAPIView


from articles.models import Article
from .serializers import ArticleSerializer


class ArtileListView(ListAPIView):
    queryset=Article.objects.all()
    serializer_class= ArticleSerializer


class ArtileDetailView(RetrieveAPIView):
    queryset=Article.objects.all()
    serializer_class= ArticleSerializer
