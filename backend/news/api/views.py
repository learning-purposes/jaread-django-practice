from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from news.models import Article
from .serializers import ArticleSerializer


# create or list functionality? according to the request
@api_view(['GET', 'POST'])
def article_list_create_api_view(request):
    if request.method == 'GET':
        articles = Article.objects.filter(active=True)
        # feed the qs to the articleserializer to return the data as response
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method =='POST':
        # inistialize serializer passing him the data of the request
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        # if serializer is not valid
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

