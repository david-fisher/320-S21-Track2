import rest_framework
from django.shortcuts import render
from django.http import *
from rest_framework import generics, renderers, status, views, viewsets
from rest_framework.response import Response as DRF_response
from rest_framework.views import APIView
from rest_framework.decorators import action
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

    @action(detail=True, renderer_classes=[renderers.JSONOpenAPIRenderer])
    def demographics(self, request, *args, **kwargs):
        student = self.get_object()
        try:
            if student.demographics is not None:
                serializer = DemographicSerializer(student.demographics)
                return DRF_response(serializer.data)
            else:
                raise Http404
        except:
            raise Http404
    


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


class StudentToCourseViewSet(viewsets.ModelViewSet):
    queryset = Student_to_Course.objects.all()
    serializer_class = StudentToCourseSerializer


class ScenarioToCourseViewSet(viewsets.ModelViewSet):
    queryset = Scenario_to_Course.objects.all()
    serializer_class = ScenarioToCourseSerializer

class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer

class StakeholdersToQuestionsViewSet(viewsets.ModelViewSet):
    queryset = Stakeholders_to_questions.objects.all()
    serializer_class = StakeholdersToQuestionsSerializer

class PagesToScenarioViewSet(viewsets.ModelViewSet):
    queryset = Pages_to_scenario.objects.all()
    serializer_class = PagesToScenarioSerializer

class ReflectionQuestionToPageViewSet(viewsets.ModelViewSet):
    queryset = Reflection_question_to_page.objects.all()
    serializer_class = ReflectionQuestionToPageSerializer

# TODO: Some viewsets are not necessary, remove after implementaion of some endpoints


class DashBoard(views.APIView):

    def get(self, request, format=None):
        student_id = self.request.query_params.get('student_id', None)
        if student_id is not None:
            try:
                scenario_list = []
                student_courses = Student.objects.get(
                    student=student_id).courses.all()
                for course in student_courses:
                    scenario_list.extend(course.scenarios.all())

                serializer = ScenarioSerializer(scenario_list, many=True)
                return DRF_response(serializer.data)
            except Student.DoesNotExist:
                raise Http404
            """  
            except:
                return DRF_response(status=status.HTTP_400_BAD_REQUEST) 
            """
        else:

            return DRF_response(status=status.HTTP_400_BAD_REQUEST)


class Get_scenario(APIView):
    def get(self, request, *args, **kwargs):

        # take scenario_id as input from URL by adding ?scenario_id=<the id #> to the end of the url.
        scenario_id = self.request.query_params.get('scenario_id')
        if(scenario_id == None):
            return DRF_response(status=status.HTTP_400_BAD_REQUEST)

        try:
            scenario = Scenario.objects.get(scenario_id=scenario_id)
            if(scenario == None):
                return Response({'status': 'details'}, status=status.HTTP_404_NOT_FOUND)
            data = ScenarioSerializer(scenario).data

            return DRF_response(data, status=status.HTTP_200_OK)
        except Scenario.DoesNotExist:
            return DRF_response({'status': 'No scenario found for this scenario id'}, status=status.HTTP_404_NOT_FOUND)


class get_pages(APIView):
    def get(self, request, *args, **kwargs):

        scenario = self.request.query_params.get('scenario_id')

        try:
            scenario = Scenario.objects.get(scenario_id=scenario)
        except Scenario.DoesNotExist:
            return DRF_response(status=status.HTTP_404_NOT_FOUND)

        page_list = []
        page_id_list = Pages.objects.filter(scenario_id=scenario)

        sorted_list = []
        for page1 in page_id_list:
            has_parent = False
            for page2 in page_id_list:
                if page2.next_page != None and page2.next_page == page1.page:
                    has_parent = True
                    break
            if not has_parent:
                sorted_list.append(page1)

        for page1 in sorted_list:
            if page1.next_page == None:
                continue
            for page2 in page_id_list:
                if page1.next_page == page2.page:
                    sorted_list.append(page2)

        for page1 in page_id_list:
            if page1 not in sorted_list:
                sorted_list.append(page1)

        for page in sorted_list:
            page_data = PagesSerializer(page).data
            page_id = page.page

            page_type = page.page_type
            # Check page.PAGE_TYPE = 'REFLECTION'
            if (page_type == 'R'):
                reflection_query = Reflection_questions.objects.filter(
                    page=page_id).values()
                page_data.update(
                    {
                        "body": reflection_query
                    }
                )
                page_list.append(page_data)

            # Check page.PAGE_TYPE = 'ACTION'
            elif (page_type == 'A'):
                action_query = Action_page.objects.filter(
                    page=page_id).values()
                page_data.update(
                    {
                        "body": action_query
                    }
                )
                page_list.append(page_data)

            # Check page.PAGE_TYPE = 'GENERIC'
            elif (page_type == 'G' or page_type == 'I'):
                generic_query = Generic_page.objects.filter(
                    page=page_id).values()
                page_data.update(
                    {
                        "body": generic_query
                    }
                )
                page_list.append(page_data)

            # Check page.PAGE_TYPE = 'STAKEHOLDER'
            elif (page_type == 'S'):
                stakeholder_query = Stakeholder_to_page.objects.filter(
                    page=page_id).values()
                page_data.update(
                    {
                        "body": stakeholder_query
                    }
                )
                page_list.append(page_data)
            # Neither of these pages, something went wrong or missing implementation
            else:
                return DRF_response(status=status.HTTP_400_BAD_REQUEST)
        return DRF_response(page_list, status=status.HTTP_200_OK)


class get_stakeholders(APIView):
    def get(self, request):
        scenario_id = self.request.query_params.get('scenario_id')
        version = self.request.query_params.get('version')
        try:
            scenario = Scenario.objects.get(scenario_id=scenario_id, version=version)
        except Scenario.DoesNotExist:
            return DRF_response(status=status.HTTP_404_NOT_FOUND)

        stakeholders_list = []
        stakeholders_id_list = Stakeholders.objects.filter(
            scenario_id=scenario_id, version=version)

        for stakeholder in stakeholders_id_list:
            convos = Conversations.objects.filter(
                stakeholder=stakeholder.stakeholder)
            cov = Coverage.objects.filter(stakeholder=stakeholder.stakeholder)
            stake_data = StakeholderSerializer(stakeholder).data

            covLst = []
            for c in cov:
                covLst.append(
                    {
                        "ISSUE": c.issue.issue,
                        "COVERAGE_SCORE": c.coverage_score
                    }
                )

            stake_data.update(
                {
                    "MATRIX": covLst
                }
            )

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
        return DRF_response(stakeholders_list, status=status.HTTP_200_OK)


class get_Issues(APIView):
    # retrieves issues for a scenario_id
    def get(self, request, format=None):
        scenario_id1 = self.request.query_params.get('scenario_id')
        try:
            scenario = Scenario.objects.get(scenario_id=scenario_id1)
        except Scenario.DoesNotExist:
            return DRF_response(status=status.HTTP_404_NOT_FOUND)
        # serializer = IssueSerializer(scenario_id, many=True)
        # return DRF_response(serializer.data)
        if(scenario_id1 == None):
            return DRF_response(status=status.HTTP_400_BAD_REQUEST)
        try:
            issues_list = []
            AllIssues = Issue.objects.filter(scenario_id=scenario_id1)

            for issue in AllIssues:
                issue_data = IssueSerializer(issue).data
                issues_list.append(issue_data)
            # serializer = IssueSerializer(issues_list, many=True)
            return DRF_response(issues_list)
        except Scenario.DoesNotExist:
            return DRF_response(status=status.HTTP_404_NOT_FOUND)


class response_to_conversations(APIView):
    def get(self, request):
        
        scenario_id = self.request.query_params.get('scenario_id')
        page_id  = self.request.query_params.get('page_id')
        student_id = self.request.query_params.get('student_id')
        
        try:
            scenario = Scenario.objects.get(scenario_id = scenario_id)
            page = Pages.objects.get(page = page_id)
            student = Student.objects.get(student = student_id)
        except Scenario.DoesNotExist:
            return rest_framework.response.Response(status=status.HTTP_404_NOT_FOUND)
        except Pages.DoesNotExist:
            return rest_framework.response.Response(status=status.HTTP_404_NOT_FOUND) 
        except Student.DoesNotExist:
            return rest_framework.response.Response(status=status.HTTP_404_NOT_FOUND)
        
        response_id_lst = Response.objects.filter(student_id = student_id, page = page_id, scenario = scenario_id)
    
        resp_to_convo_final_lst = []
        for response in response_id_lst:
            resp_json = ResponseSerializer(response).data
            resp_to_convos_obj_lst = Responses_to_conversations.objects.filter(response_id = response.response_id)
            for j in resp_to_convos_obj_lst:
                convos = Conversations.objects.filter(conversation = j.conversation.conversation)
                convo_lst = []
                for i in convos:
                    convo_json = ConversationSerializer(i).data
                    convo_lst.append(convo_json)

                resp_to_convo_json = Responses_to_conversationsSerializer(j).data
                resp_to_convo_json.update(
                    {
                        "response": resp_json,
                        "conversation": convo_lst
                    }
                )
                resp_to_convo_final_lst.append(resp_to_convo_json)
        return rest_framework.response.Response(resp_to_convo_final_lst, status=status.HTTP_200_OK)


    # put a student conversation into the database
    def put(self, request,  *args, **kwargs):
        # takes in a JSON of the format:
        # {
        #     "scenario_id": 1,
        #     "student_id": 1,
        #     "conversation_id": 1,
        #     "score": 1,
        #     "course_id": 1,
        #     "page_id": 1
        # }

        scenario_id = request.data.get('scenario_id')
        student_id = request.data.get('student_id')
        conversation_id = request.data.get('conversation_id')
        score = request.data.get('score')
        course_id = request.data.get('course_id')
        page_id = request.data.get('page_id')

        # extra check for if the given JSON has the required fields
        if(scenario_id is None or student_id is None or conversation_id is None or score is None or course_id is None or page_id is None):
            return DRF_response({'detail': "Missing one or more parameters"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            conversation = Conversations.objects.get(
                conversation=conversation_id)
            stakeholder = conversation.stakeholder.stakeholder

            # formats the response entry to match the model
            response = {
                "student": student_id,
                "scenario": scenario_id,
                "page": page_id,
                "course": course_id,
                "choice": str(conversation_id)
            }

            # deserialize the response entry, and check if the response entry is valid
            responseSerializer = ResponseSerializer(data=response)
            if not responseSerializer.is_valid():
                return DRF_response(responseSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

            # saves the response to the database
            responseSerializer.save()

            # formats the entries of response_to_conv to match the model
            response_to_conv = {
                "response": responseSerializer.data['response_id'],
                "stakeholder": stakeholder,
                "score": score,
                "conversation": conversation_id
            }

            # deserialize the entry and check if the entry is valid
            responseToConvSerializer = Responses_to_conversationsSerializer(
                data=response_to_conv)
            if not responseToConvSerializer.is_valid():
                return DRF_response(responseToConvSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

            # saves the response_to_conversation entry
            responseToConvSerializer.save()
            return DRF_response(responseToConvSerializer.data, status=status.HTTP_200_OK)
        except Conversations.DoesNotExist:
            return DRF_response({'detail': "conversation_id not found"}, status=status.HTTP_404_NOT_FOUND)
        # Only need exception check for Conversations.DoesNotExist, all other bad inputs are handled by the serializer.valid()

class reflection(APIView):
    #retrieve a reflection for a particular response from the database
    def get(self, request, *args, **kwargs):
        page_id = self.request.query_params.get('page_id') 
        student_id = self.request.query_params.get('student_id')
        scenario_id = self.request.query_params.get('scenario_id')


        # extra check for if the given JSON has the required fields
        if(scenario_id is None or page_id is None or student_id is None ):
            return DRF_response({'detail': "Missing one or more parameters"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            response = Response.objects.get(page= page_id, student = student_id, scenario = scenario_id)
        except Response.DoesNotExist:
            return DRF_response(status=status.HTTP_404_NOT_FOUND)
        
        try:
            ref = Reflections_taken.objects.filter(response = response.response_id).first()
            reflection_data = ReflectionsTakenSerializer(ref).data
            return DRF_response(reflection_data)
        except Scenario.DoesNotExist:
            return DRF_response(status=status.HTTP_404_NOT_FOUND)