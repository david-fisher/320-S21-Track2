from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from api.models import *
from api.serializers import *
from rest_framework.views import APIView
from rest_framework import status
import rest_framework

# Create your views here.


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class DemographicViewSet(viewsets.ModelViewSet):
    queryset = Demographic.objects.all()
    serializer_class = DemographicSerializer

class ScenariosViewSet(viewsets.ModelViewSet):
    queryset= Scenario.objects.all()
    serializer_class = ScenarioSerializer

class ResponsesViewSet(viewsets.ModelViewSet):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer

class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

class ConversationsViewSet(viewsets.ModelViewSet):
    queryset = Conversations.objects.all()
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

    
class Generic_pageViewSet(viewsets.ModelViewSet):
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
class CoverageViewSet(viewsets.ModelViewSet):
    queryset = Coverage.objects.all()
    serializer_class = ConversationSerializer


class StakeholdersViewSet(viewsets.ModelViewSet):
    queryset= Stakeholders.objects.all()
    serializer_class = StakeholderSerializer


class get_scenario(APIView):
    def get(self, request, *args, **kwargs):
        
        # take scenario_id as input from URL by adding ?scenario_id=<the id #> to the end of the url.
        scenario_id = self.request.query_params.get('scenario_id')
        if(scenario_id != None):
            return rest_framework.response.Response({"type": str(type(request))},status=status.HTTP_400_BAD_REQUEST)
        
        try:
            scenario = Scenario.objects.get(scenario = scenario_id)
            if(scenario == None):
                return Response({'status': 'details'}, status=status.HTTP_404_NOT_FOUND)
            data = ScenarioSerializer(scenario).data
            
            return rest_framework.response.Response(data, status = status.HTTP_200_OK)
        except Scenario.DoesNotExist:
            return rest_framework.response.Response({'status': 'No scenario found for this scenario id'}, status=status.HTTP_404_NOT_FOUND)