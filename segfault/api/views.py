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



class PagesViewSet(viewsets.ModelViewSet):
    queryset = pages.objects.all()
    serializer_class = PagesSerializer

class Stakeholder_pageViewSet(viewsets.ModelViewSet):
    queryset = stakeholder_page.objects.all()
    serializer_class = Stakeholder_pageSerializer
    
class Reflection_QuestionsViewSet(viewsets.ModelViewSet):
    queryset = reflection_questions.objects.all()
    serializer_class = Reflection_questionsSerializer

    
class generic_pageViewSet(viewsets.ModelViewSet):
    queryset = generic_page.objects.all()
    serializer_class = Generic_pageSerializer
    
class Action_pageViewSet(viewsets.ModelViewSet):
    queryset = action_page.objects.all()
    serializer_class = Action_pageSerializer

class Page_reflectionViewSet(generics.CreateAPIView):
    model = pages
    serializer_class = Pages_reflectionSerializer

class Page_actionViewSet(generics.CreateAPIView):
    model = pages
    serializer_class = Pages_actionSerializer   

class Page_genericViewSet(generics.CreateAPIView):
    model = pages
    serializer_class = Pages_genericSerializer

class Page_StakeholderViewSet(generics.CreateAPIView):
    model = pages
    serializer_class = Pages_stakeholderSerializer
    


