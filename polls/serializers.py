from rest_framework import serializers
from rest_framework.views import APIView

from polls.models import Answer, Question

from users.serializers import DetailCitizenSerializer


class AllQuestionSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ('title', 'author')

    def get_author(self, obj):
        return DetailCitizenSerializer(obj.author, context=self.context).data


class DetailQuestionSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ('title', 'author', 'description', 'datetime_created', 'datetime_modified')

    def get_author(self, obj):
        return DetailCitizenSerializer(obj.author, context=self.context).data


class AnswerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('title', 'description', 'datetime_created', 'datetime_modified')