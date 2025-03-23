from rest_framework.response import Response
from .models import Article,Category
from accounts.models import CustomUser
from .serializers import ArticleSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsEditor
# Create your views here.

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def article_view(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles,many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsEditor])
def article_create(request):
    data = request.data.copy()
    data['author']=request.user
    print(data)
    serializer = ArticleSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response( status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes([IsEditor])
def article_detials(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
