from django.urls import path
from  articles.api.views import ArticleListView ,ArticleDetailView


urlpatterns = [
    path('',ArticleListView.as_view()),
    path('<pk>',ArticleDetailView.as_view()),
]