from rest_framework import serializers
from webapp.models.comment import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', 'author', 'created_at', 'updated_at']
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']

    # def validate_text(self, value):
    #     if len(value) < 5:
    #         raise serializers.ValidationError('Длина названия должна быть не менее 5 символов')
    #     return value

    def validate(self, attrs):
        return super().validate(attrs)
