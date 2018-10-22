from blogapp.models import Article
from rest_framework import serializers
from django.http import JsonResponse
from rest_framework.decorators import api_view


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'  # {'title', 'content'} yuanzu


@api_view(['GET'])
def article(request):
    article_list = Article.objects.all()
    serializer = ArticleSerializer(article_list, many=True)
    # return JsonResponse(serializer.data)
    return JsonResponse(serializer.data, safe=False)
