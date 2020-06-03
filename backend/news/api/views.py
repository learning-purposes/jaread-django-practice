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

    elif request.method == 'POST':
        # inistialize serializer passing him the data of the request
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # if serializer is not valid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_api_view(request, pk):
    # check if pk is valid
    try:
        article = Article.objects.get(pk=pk)
    except article.DoesNotExist:
        # define customized error message
        return Response({'error': {
            'code': 404,
            'message': 'Article not found!'}},
            status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
