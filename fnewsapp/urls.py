from django.urls import path
from . import views

urlpatterns = [
    path('articleview/', views.article_view),
    path("articlelist/<int:id>/",views.articlelist)

]