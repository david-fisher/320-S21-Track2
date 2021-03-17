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


# response, reflections taken, response_to_action_page, conversations had, student times

class ReflectionsTakenViewSet(viewsets.ModelViewSet):
    queryset = reflections_taken.objects.all()
    serializer_class = ReflectionsTakenSerializer

class ResponseToActionPageViewSet(viewsets.ModelViewSet):
    queryset = response_to_action_page.objects.all()
    serializer_class = ResponseToActionPageSerializer

class ConversationsHadViewSet(viewsets.ModelViewSet):
    queryset = conversations_had.objects.all()
    serializer_class = ConversationsHadSerializer

class StudentTimesViewSet(viewsets.ModelViewSet):
    queryset = student_times.objects.all()
    serializer_class = StudentTimesSerializer