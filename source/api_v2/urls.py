from django.urls import path

from api_v2.views import get_token_view, ArticleView, CommentView


app_name = 'v2'


urlpatterns = [
    path('articles/', ArticleView.as_view(), name='articles'),
    path('articles/<int:pk>/', ArticleView.as_view(), name='article'),
    path('get-csrf/', get_token_view, name='get-csrf'),

    path('article/<int:article_pk>/comment/', CommentView.as_view(), name='comments'),
    path('article/<int:article_pk>/comment/<int:comment_pk>/', CommentView.as_view(), name='detail_comments'),
    path('article/<int:article_pk>/', CommentView.as_view(), name='create_comment'),


]