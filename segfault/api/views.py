from django.shortcuts import render
from rest_framework import viewsets
from api.models import *
from api.serializers import *

# Create your views here.
class ScenariosViewSet(viewsets.ModelViewSet):
    queryset= Scenario.objects.all()
    serializer_class = ScenarioSerializer

class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class DemographicViewSet(viewsets.ModelViewSet):
    queryset = Demographic.objects.all()
    serializer_class = DemographicSerializer
class ResponsesViewSet(viewsets.ModelViewSet):
    queryset = Response.objects.all()
    serializer_class = CourseSerializer
class IssuesViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
class ConversationsViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
