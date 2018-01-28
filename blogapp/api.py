from blogapp.models import Article
from rest_framework import serializers
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view


class ArticleSerializer(serializers.ModelDurationField):
    class Meta:
        model = Article
        fields = '__all__'  # {'title', 'content'} yuanzu


@api_view(['GET'])
def article():
    article_list = Article.objects.all()
    serializers = ArticleSerializer(article_list, many=True)
    return JsonResponse(serializers.data)
