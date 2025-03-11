from django.db import models
from accounts.models import CustomUser,LocalNewsSite
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    icon = models.ImageField(upload_to='category_icon/', null=True, blank=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True,blank=True)
    content = models.TextField()
    #site = models.ForeignKey(LocalNewsSite,on_delete=models.CASCADE, related_name='articles')
    cover = models.ImageField(upload_to='article_cover/', null=True, blank=True)
    image = models.ImageField(upload_to='article_image/', null=True, blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='articles')
    categories = models.ManyToManyField(Category, related_name='articles')
    published_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)

    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title