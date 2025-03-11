from rest_framework import serializers
from .models import Article,Category
from accounts.models import CustomUser

class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    author = serializers.StringRelatedField()
    class Meta:
        model = Article
        fields = '__all__'