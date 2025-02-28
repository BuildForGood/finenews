from django.db import models
from accounts.models import Profile
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    icon = models.ImageField(upload_to='category_icon/', null=True, blank=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    cover = models.ImageField(upload_to='article_cover/', null=True, blank=True)
    image = models.ImageField(upload_to='article_image/', null=True, blank=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='articles')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='articles')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title