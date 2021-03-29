from django.shortcuts import render
from django.http import *
from rest_framework import views, viewsets, generics, status
import rest_framework.response
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
    queryset = Scenario.objects.all()
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
    queryset = Pages.objects.all()
    serializer_class = PagesSerializer


class Stakeholder_to_pageViewSet(viewsets.ModelViewSet):
    queryset = Stakeholder_to_page.objects.all()
    serializer_class = Stakeholder_to_pageSerializer


class Reflection_QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Reflection_questions.objects.all()
    serializer_class = Reflection_questionsSerializer


class Generic_pageViewSet(viewsets.ModelViewSet):
    queryset = Generic_page.objects.all()
    serializer_class = Generic_pageSerializer


class Action_pageViewSet(viewsets.ModelViewSet):
    queryset = Action_page.objects.all()
    serializer_class = Action_pageSerializer


class Page_reflectionViewSet(generics.CreateAPIView):
    model = Pages
    serializer_class = Pages_reflectionSerializer


class Page_actionViewSet(generics.CreateAPIView):
    model = Pages
    serializer_class = Pages_actionSerializer


class Page_genericViewSet(generics.CreateAPIView):
    model = Pages
    serializer_class = Pages_genericSerializer


class Page_StakeholderViewSet(generics.CreateAPIView):
    model = Pages
    serializer_class = Pages_stakeholderSerializer
    
class ReflectionsTakenViewSet(viewsets.ModelViewSet):
    queryset = Reflections_taken.objects.all()
    serializer_class = ReflectionsTakenSerializer


class ResponseToActionPageViewSet(viewsets.ModelViewSet):
    queryset = Response_to_action_page.objects.all()
    serializer_class = ResponseToActionPageSerializer


class Responses_to_conversationsViewSet(viewsets.ModelViewSet):
    queryset = Responses_to_conversations.objects.all()
    serializer_class = Responses_to_conversationsSerializer

class Student_page_progressViewSet(viewsets.ModelViewSet):
    queryset = Student_page_progress.objects.all()
    serializer_class = Student_page_progressSerializer

class StudentTimesViewSet(viewsets.ModelViewSet):
    queryset = Student_times.objects.all()
    serializer_class = StudentTimesSerializer


class CoverageViewSet(viewsets.ModelViewSet):
    queryset = Coverage.objects.all()
    serializer_class = CoverageSerializer


class StakeholdersViewSet(viewsets.ModelViewSet):
    queryset = Stakeholders.objects.all()
    serializer_class = StakeholderSerializer

# TODO: Some viewsets are not necessary, remove after implementaion of some endpoints


class DashBoard(views.APIView):

    def get(self, request, format=None):
        student_id = self.request.query_params.get('student_id', None)
        if student_id is not None:
            try:
                scenario_list = []
                student_courses= Student.objects.get(student=student_id).courses.all() 
                for course in student_courses:
                    scenario_list.extend(course.scenarios.all())
                
                serializer = ScenarioSerializer(scenario_list, many=True)
                return rest_framework.response.Response(serializer.data)
            except Student.DoesNotExist:
                raise Http404
            """  
            except:
                return rest_framework.response.Response(status=status.HTTP_400_BAD_REQUEST) 
            """
        else: 
            
            return rest_framework.response.Response(status=status.HTTP_400_BAD_REQUEST)


class Get_scenario(APIView):
    def get(self, request, *args, **kwargs):
        
        # take scenario_id as input from URL by adding ?scenario_id=<the id #> to the end of the url.
        scenario_id = self.request.query_params.get('scenario_id')
        if(scenario_id == None):
            return rest_framework.response.Response(status=status.HTTP_400_BAD_REQUEST)
        
        try:
            scenario = Scenario.objects.get(scenario_id = scenario_id)
            if(scenario == None):
                return Response({'status': 'details'}, status=status.HTTP_404_NOT_FOUND)
            data = ScenarioSerializer(scenario).data
            
            return rest_framework.response.Response(data, status = status.HTTP_200_OK)
        except Scenario.DoesNotExist:
            return rest_framework.response.Response({'status': 'No scenario found for this scenario id'}, status=status.HTTP_404_NOT_FOUND)


        

class get_pages(APIView):
    def get(self, request, *args, **kwargs):

        scenario = self.request.query_params.get('scenario_id')
        
        try:
            scenario = Scenario.objects.get(scenario_id = scenario)
        except Scenario.DoesNotExist:
            return rest_framework.response.Response(status=status.HTTP_404_NOT_FOUND)

        page_list = []
        page_id_list = Pages.objects.filter(scenario_id = scenario)

        for page in page_id_list:
            page_data = PagesSerializer(page).data
            page_id = page.page
        
            page_type = page.page_type
            # Check page.PAGE_TYPE = 'REFLECTION'
            if (page_type == 'R'):
                reflection_query = Reflection_questions.objects.filter(page = page_id).values()
                page_data.update(
                    {
                        "body": reflection_query
                    }
                )
                page_list.append(page_data)

            # Check page.PAGE_TYPE = 'ACTION'
            elif (page_type == 'A'):
                action_query = Action_page.objects.filter(page = page_id).values()
                page_data.update(
                    {
                        "body": action_query
                    }
                )                
                page_list.append(page_data)
        
            # Check page.PAGE_TYPE = 'GENERIC'
            elif (page_type == 'G' or page_type == 'I'):
                generic_query = Generic_page.objects.filter(page = page_id).values()
                page_data.update(
                    {
                        "body":generic_query
                    }
                )
                page_list.append(page_data)
        
            # Check page.PAGE_TYPE = 'STAKEHOLDER'
            elif (page_type == 'S'):
                stakeholder_query = Stakeholder_to_page.objects.filter(page = page_id).values()
                page_data.update(
                    {
                        "body": stakeholder_query
                    }
                )
                page_list.append(page_data)
        
            # Neither of these pages, something went wrong or missing implementation
            else:
                return rest_framework.response.Response(status=status.HTTP_400_BAD_REQUEST)
        return rest_framework.response.Response(page_list, status=status.HTTP_200_OK)

class get_stakeholders(APIView):
    def get(self, request):
        scenario_id1 = self.request.query_params.get('scenario_id')
        try:
            scenario = Scenario.objects.get(scenario_id = scenario_id1)
        except Scenario.DoesNotExist:
            return rest_framework.response.Response(status=status.HTTP_404_NOT_FOUND)
        
        stakeholders_list = []
        stakeholders_id_list = Stakeholders.objects.filter(scenario_id = scenario_id1)

        for stakeholder in stakeholders_id_list:
            convos = Conversations.objects.filter(stakeholder = stakeholder.stakeholder)
            stake_data = StakeholderSerializer(stakeholder).data
            
            convoLst = []
            for c in convos:
                convoLst.append(
                    {
                        "CONVERSATION": c.conversation,
                        "QUESTION": c.question,
                        "RESPONSE": c.response 
                    }
                )
            
            stake_data.update(
                {
                    "CONVERSATIONS": convoLst
                }
            )
            stakeholders_list.append(stake_data)
        return rest_framework.response.Response(stakeholders_list, status=status.HTTP_200_OK)

class get_Issues(APIView):

    #retrieves issues for a scenario_id
    def get(self, request, format = None):
        scenario_id1 = self.request.query_params.get('scenario_id')
        try:
            scenario = Scenario.objects.get(scenario_id = scenario_id1)
        except Scenario.DoesNotExist:
            return rest_framework.response.Response(status=status.HTTP_404_NOT_FOUND)
        # serializer = IssueSerializer(scenario_id, many=True)
        # return rest_framework.response.Response(serializer.data) 
        if(scenario_id1 == None):
            return rest_framework.response.Response(status=status.HTTP_400_BAD_REQUEST) 
        try:
            issues_list = []
            AllIssues = Issue.objects.filter(scenario_id = scenario_id1)

            for issue in AllIssues:
                issue_data = IssueSerializer(issue).data
                issues_list.append(issue_data)
            # serializer = IssueSerializer(issues_list, many=True)
            return rest_framework.response.Response(issues_list)
        except Scenario.DoesNotExist:
            return rest_framework.response.Response(status=status.HTTP_404_NOT_FOUND)

