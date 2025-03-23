from rest_framework import serializers
from .models import Article,Category
from accounts.models import CustomUser

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', queryset=CustomUser.objects.all())
    categories = serializers.SlugRelatedField(slug_field='name',queryset=Category.objects.all(), many=True)
    #sites = serializers.StringRelatedField()
    class Meta:
        model = Article
        fields = ['title','content','categories','author']

