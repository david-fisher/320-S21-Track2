from django.shortcuts import render
from django.http import *
from rest_framework import views, viewsets, generics, status
import rest_framework.response
from api.models import *
from api.serializers import *

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
