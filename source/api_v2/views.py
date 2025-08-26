import json
from json import JSONDecodeError

from django.contrib.auth import get_user_model
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse, HttpResponseBadRequest
from django.template.defaulttags import comment

from django.views import View
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from webapp.models.article import Article
from api_v2.serialisers import ArticleSerializer
from webapp.models.comment import Comment
from api_v2.serialisers.comments import CommentSerializer


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')


class ArticleView(APIView):
    def get(self, request, *args, pk=None, **kwargs):
        if pk:
            article = get_object_or_404(Article, pk=pk)
            serializer = ArticleSerializer(article)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            articles = Article.objects.all()
            serializer = ArticleSerializer(articles, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):
        serializer = ArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_user_model().objects.last()
        article = serializer.save(author=user)
        return Response({'id': article.id}, status=status.HTTP_201_CREATED)


    def put(self, request, *args, pk, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(data=request.data, instance=article)
        if serializer.is_valid():
            article = serializer.save()
            return Response(serializer.data)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, *args, pk=None, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article)
        Article.objects.filter(id=article.id).delete()
        return Response('deleted', status=status.HTTP_204_NO_CONTENT)


class CommentView(APIView):
    def get(self, request, *args, article_pk=None, comment_pk=None, **kwargs):
        if not comment_pk:
            article = get_object_or_404(Article, pk=article_pk)
            comments = Comment.objects.filter(article=article)
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            article = get_object_or_404(Article, pk=article_pk)
            comment = get_object_or_404(Comment, pk=comment_pk, article=article)
            serializer = CommentSerializer(comment)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, article_pk=None, **kwargs):
        article = get_object_or_404(Article, pk=article_pk)
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        comment = serializer.save(article=article)
        return Response({
            'id': comment.id,
            'text': comment.text,
            'author': comment.author.username,
            'article_id': comment.article_id,
            'created_at': comment.created_at,
            'updated_at': comment.updated_at,},
            status=status.HTTP_201_CREATED)

    def put(self, request, *args, article_pk=None, comment_pk=None, **kwargs):
        article = get_object_or_404(Article, pk=article_pk)
        comment = get_object_or_404(Comment, pk=comment_pk, article=article)
        serializer = CommentSerializer(data=request.data, instance=comment)
        serializer.is_valid(raise_exception=True)
        comment = serializer.save()
        return Response(serializer.data)


    def delete(self, request, *args, article_pk=None, comment_pk=None, **kwargs):
        article = get_object_or_404(Article, pk=article_pk)
        comment = get_object_or_404(Comment, pk=comment_pk, article=article)
        Comment.objects.filter(id=comment.id).delete()
        return Response('deleted', status=status.HTTP_204_NO_CONTENT)



        # if pk:
        #     article = get_object_or_404(Article, pk=pk)
        #     comment = Comment.objects.create(article=article)
        #     serializer = ArticleSerializer(article)
        #     return Response(serializer.data)
        # else:
        #     articles = Article.objects.all()
        #     serializer = ArticleSerializer(articles, many=True)
        #     return Response(serializer.data)


# class ArticleView(View):
#     def get(self, request, *args, **kwargs):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     def post(self, request, *args, **kwargs):
#         body = json.loads(request.body)
#         serializer = ArticleSerializer(data=body)
#         if serializer.is_valid():
#             # user = request.user
#             user = get_user_model().objects.last()
#             article = serializer.save(author=user)
#             return JsonResponse({'id': article.id}, status=201)
#         else:
#             return JsonResponse({'error': serializer.errors}, status=400)
#
#     def put(self, request, *args, pk, **kwargs):
#         article = get_object_or_404(Article, pk=pk)
#         body = json.loads(request.body)
#         serializer = ArticleSerializer(data=body, instance=article)
#         if serializer.is_valid():
#             article = serializer.save()
#             return JsonResponse(serializer.data, status=200)
#         else:
#             return JsonResponse({'error': serializer.errors}, status=400)

