import json
from json import JSONDecodeError

from django.contrib.auth import get_user_model
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse, HttpResponseBadRequest
from django.views import View
from django.views.decorators.csrf import ensure_csrf_cookie
from webapp.models.article import Article

from api_v2.serialisers import ArticleSerializer


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        body = json.loads(request.body)
        serializer = ArticleSerializer(data=body)
        if serializer.is_valid():
            # user = request.user
            user = get_user_model().objects.last()
            article = serializer.save(author=user)
            return JsonResponse({'id': article.id}, status=201)
        else:
            return JsonResponse({'error': serializer.errors}, status=400)



