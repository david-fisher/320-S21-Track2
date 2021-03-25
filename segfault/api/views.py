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
            scenario = Scenario.objects.get(scenario = scenario_id)
            if(scenario == None):
                return Response({'status': 'details'}, status=status.HTTP_404_NOT_FOUND)
            data = ScenarioSerializer(scenario).data
            
            return rest_framework.response.Response(data, status = status.HTTP_200_OK)
        except Scenario.DoesNotExist:
            return rest_framework.response.Response({'status': 'No scenario found for this scenario id'}, status=status.HTTP_404_NOT_FOUND)



class get_pages(APIView):
    def get(self, request, *args, **kwargs):

        scenario_id = self.request.query_params.get('scenario_id')
        
        try:
            scenario = Scenario.objects.get(scenario = scenario_id)
        except Scenario.DoesNotExist:
            return rest_framework.response.Response(status=status.HTTP_404_NOT_FOUND)

        page_list = []
        page_id_list = Pages.objects.filter(SCENARIO = scenario_id)

        for page in page_id_list:
            page_data = PagesSerializer(page).data
            page_id = page.PAGE
        
            page_type = page.PAGE_TYPE
            # Check page.PAGE_TYPE = 'REFLECTION'
            if (page_type == 'R'):
                reflection_query = reflection_questions.objects.filter(PAGE = page_id).values()
                page_data.update(
                    {
                        "REFLECTION_QUESTIONS": reflection_query
                    }
                )
                page_list.append(page_data)

            # Check page.PAGE_TYPE = 'ACTION'
            elif (page_type == 'A'):
                action_query = action_page.objects.filter(PAGE = page_id).values()
                page_data.update(
                    {
                        "CHOICES": action_query
                    }
                )                
                page_list.append(page_data)
        
            # Check page.PAGE_TYPE = 'GENERIC'
            elif (page_type == 'G' or page_type == 'I'):
                generic_query = generic_page.objects.filter(PAGE = page_id).values()
                page_data.update(
                    {
                        "BODIES":generic_query
                    }
                )
                page_list.append(page_data)
        
            # Check page.PAGE_TYPE = 'STAKEHOLDER'
            elif (page_type == 'S'):
                stakeholder_query = stakeholder_page.objects.filter(PAGE = page_id).values()
                page_data.update(
                    {
                        "STAKEHOLDERS": stakeholder_query
                    }
                )
                page_list.append(page_data)
        
            # Neither of these pages, something went wrong or missing implementation
            else:
                return rest_framework.response.Response(status=status.HTTP_400_BAD_REQUEST)

        return rest_framework.response.Response(page_list, status=status.HTTP_200_OK)

class get_Issues(APIView):

    #retrieves issues for a scenario_id
    def get(self, request, format = None):
        scenario_id = self.request.query_params.get('scenario_id')
        # serializer = IssueSerializer(scenario_id, many=True)
        # return rest_framework.response.Response(serializer.data) 
        if(scenario_id == None):
            return rest_framework.response.Response(status=status.HTTP_400_BAD_REQUEST) 
        try:
            issues_list = []
            AllIssues = Issue.objects.filter(scenario = scenario_id)

            for issue in AllIssues:
                issue_data = IssueSerializer(issue).data
                issues_list.append(issue_data)
            # serializer = IssueSerializer(issues_list, many=True)
            return rest_framework.response.Response(issues_list)
        except Scenario.DoesNotExist:
            return rest_framework.response.Response(status=status.HTTP_404_NOT_FOUND)

    