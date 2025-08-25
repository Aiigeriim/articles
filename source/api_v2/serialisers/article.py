from rest_framework import serializers
from webapp.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'author', 'status', 'tags', 'created_at', 'updated_at']
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError('Длина названия должна быть не менее 5 символов')
        return value

    def validate(self, attrs):
        return super().validate(attrs)

# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=True, max_length=50)
#     content = serializers.CharField(required=True)
#     author = serializers.PrimaryKeyRelatedField(read_only=True)
#     status = serializers.ChoiceField(choices=statuses, default=statuses[0][0])
#     tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all(), required=False)
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)
#
#     def validate_title(self, value):
#         if len(value) < 5:
#             raise serializers.ValidationError('Длина названия должна быть не менее 5 символов')
#          return value


#     def validate(self, attrs):
#         return super().validate(attrs)


    # def create(self, validated_data):
    #     tags = validated_data.pop('tags', [])
    #     article = Article.objects.create(**validated_data)
    #     article.tags.set(tags)
    #     return article
    #
    # def update(self, instance, validated_data):
    #     tags = validated_data.pop('tags', [])
    #     for attr, value in validated_data.items():
    #         setattr(instance, attr, value)
    #     instance.save()
    #     instance.tags.set(tags)
    #     return instance





