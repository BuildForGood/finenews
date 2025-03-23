from django.urls import path
from . import views

urlpatterns = [
    path('articleview/', views.article_view),
    path('articlecreate/', views.article_create),
    path("articledetials/<int:id>/",views.article_detials)

]