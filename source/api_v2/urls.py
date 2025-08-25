from django.urls import path

from source.api_v2.views import get_token_view

app_name = 'v2'


urlpatterns = [
    # path('articles/', ArticleView.as_view(), name='articles'),
    # path('articles/<int:pk>/', ArticleView.as_view(), name='article'),
    path('get-csrf/', get_token_view, name='get-csrf'),
]