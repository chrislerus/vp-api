from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from polls.models import Question, Answer
from polls.serializers import AllQuestionSerializer, DetailQuestionSerializer, AnswerListSerializer

from users.models import Mayor

class QuestionsList(APIView):
    """
    Return list of questions
    """

    def get(self, request, format=None):
        questions = Question.objects.filter()
        serializer = AllQuestionSerializer(questions, many=True)
        return Response(serializer.data)


class QuestionDetail(APIView):
    """
    Return one question details
    """

    def get_object(self, pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = DetailQuestionSerializer(question)
        return Response(serializer.data)


class AnswerList(APIView):
    """
    Return list of answers for one question
    """

    def get(self, request, pk, format=None):
        answers = Answer.objects.filter(question=Question.objects.get(pk=pk))
        serializer = AnswerListSerializer(answers, many=True)
        return Response(serializer.data)