from rest_framework.response import Response, responses
from rest_framework.decorators import api_view
from .models import quiz
from .serializers import QuizSerializer
import random

from quiz import serializers
# Create your views here.

@api_view(['GET'])
def helloAPI(request):
    return Response('Hello World!')


@api_view(['GET'])
def randomQuiz(request, id):
    totalQuizs = quiz.objects.all() 
    randomQuizs = random.sample(list(totalQuizs), id)
    serializer = QuizSerializer(randomQuizs, many = True)
    return Response(serializer.data)