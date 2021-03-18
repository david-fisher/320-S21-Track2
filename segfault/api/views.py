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
    queryset = Issues.objects.all()
    serializer_class = IssueSerializer
class ConversationsViewSet(viewsets.ModelViewSet):
    queryset = Conversations.objects.all()
    serializer_class = ConversationSerializer

class CoverageViewSet(viewsets.ModelViewSet):
    queryset = Coverage.objects.all()
    serializer_class = ConversationSerializer

class Scenarios_forViewSet(viewsets.ModelViewSet):
    queryset= Scenarios_for.objects.all()
    serializer_class = ScenarioSerializer

class StakeholdersViewSet(viewsets.ModelViewSet):
    queryset= Stakeholders.objects.all()
    serializer_class = ScenarioSerializer