from rest_framework import serializers

from webapp.models.article import statuses
from webapp.models import Tag, Article


class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=50)
    content = serializers.CharField(required=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    status = serializers.ChoiceField(choices=statuses, default=statuses[0][0])
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all(), required=False)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        tags = validated_data.pop('tags')
        article = Article.objects.create(**validated_data)
        article.tags.set(tags)
        return article



