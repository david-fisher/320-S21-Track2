import rest_framework
import datetime
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
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professors.objects.all()
    serializer_class = ProfessorSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
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
    queryset = Demographics.objects.all()
    serializer_class = DemographicSerializer


class ScenariosViewSet(viewsets.ModelViewSet):
    queryset = Scenarios.objects.all()
    serializer_class = ScenarioSerializer


class ResponsesViewSet(viewsets.ModelViewSet):
    queryset = Responses.objects.all()
    serializer_class = ResponseSerializer


class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issues.objects.all()
    serializer_class = IssueSerializer


class ConversationsViewSet(viewsets.ModelViewSet):
    queryset = Conversations.objects.all()
    serializer_class = ConversationSerializer


class PagesViewSet(viewsets.ModelViewSet):
    queryset = Pages.objects.all()
    serializer_class = PagesSerializer


class Stakeholder_to_pageViewSet(viewsets.ModelViewSet):
    queryset = StakeholderToPage.objects.all()
    serializer_class = Stakeholder_to_pageSerializer


class Reflection_QuestionsViewSet(viewsets.ModelViewSet):
    queryset = ReflectionQuestions.objects.all()
    serializer_class = Reflection_questionsSerializer


class Generic_pageViewSet(viewsets.ModelViewSet):
    queryset = GenericPage.objects.all()
    serializer_class = Generic_pageSerializer


class Action_pageViewSet(viewsets.ModelViewSet):
    queryset = ActionPage.objects.all()
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
    queryset = ReflectionsTaken.objects.all()
    serializer_class = ReflectionsTakenSerializer


class ResponseToActionPageViewSet(viewsets.ModelViewSet):
    queryset = ResponseToActionPage.objects.all()
    serializer_class = ResponseToActionPageSerializer


class Responses_to_conversationsViewSet(viewsets.ModelViewSet):
    queryset = ResponsesToConversations.objects.all()
    serializer_class = Responses_to_conversationsSerializer


# class Student_page_progressViewSet(viewsets.ModelViewSet):
#     queryset = Student_page_progress.objects.all()
#     serializer_class = Student_page_progressSerializer


class StudentTimesViewSet(viewsets.ModelViewSet):
    queryset = StudentTimes.objects.all()
    serializer_class = StudentTimesSerializer


class CoverageViewSet(viewsets.ModelViewSet):
    queryset = Coverage.objects.all()
    serializer_class = CoverageSerializer


class StakeholdersViewSet(viewsets.ModelViewSet):
    queryset = Stakeholders.objects.all()
    serializer_class = StakeholderSerializer


class StudentToCourseViewSet(viewsets.ModelViewSet):
    queryset = StudentsToCourse.objects.all()
    serializer_class = StudentToCourseSerializer


class ScenariosForViewSet(viewsets.ModelViewSet):
    queryset = ScenariosFor.objects.all()
    serializer_class = ScenarioForSerializer

class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer

class StakeholdersToQuestionsViewSet(viewsets.ModelViewSet):
    queryset = StakeholdersToQuestions.objects.all()
    serializer_class = StakeholdersToQuestionsSerializer

class PagesToScenarioViewSet(viewsets.ModelViewSet):
    queryset = PagesToScenario.objects.all()
    serializer_class = PagesToScenarioSerializer

class ReflectionQuestionToPageViewSet(viewsets.ModelViewSet):
    queryset = ReflectionQuestionToPage.objects.all()
    serializer_class = ReflectionQuestionToPageSerializer

class ProfessorsToScenarioViewSet(viewsets.ModelViewSet):
    queryset = ProfessorsToScenario.objects.all()
    serializer_class = ProfessorsToScenarioSerializer

class ProfessorsToCoursesViewSet(viewsets.ModelViewSet):
    queryset = ProfessorsToCourses.objects.all()
    serializer_class = ProfessorsToCoursesSerializer

# TODO: Some viewsets are not necessary, remove after implementaion of some endpoints


class DashBoard(views.APIView):

    def get(self, request, format=None):
        student_id = self.request.query_params.get('student_id', None)
        if student_id is not None:
            if type(student_id) != type("a string"):
                try:
                    student_id = str(student_id)
                except:
                    return DRF_response(status=status.HTTP_400_BAD_REQUEST)
            try:
                scenario_list = []
                student_courses = Students.objects.get(
                    student=student_id).courses.all()
                for course in student_courses:
                    scenario_list.extend(course.scenarios.all())
                
                scenario_data_list = ScenarioSerializer(scenario_list, many=True).data

                for scenario in scenario_data_list:
                    try:
                        stuTime = StudentTimes.objects.get(student = student_id, scenario = scenario['scenario_id'])
                        result = stuTime.end_time != None
                    except:
                        result = False
                    scenario['student_finished'] = result

                return DRF_response(scenario_data_list)
            except Students.DoesNotExist:
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
            scenario = Scenarios.objects.get(scenario_id=scenario_id)
            if(scenario == None):
                return Responses({'status': 'details'}, status=status.HTTP_404_NOT_FOUND)
            data = ScenarioSerializer(scenario).data

            return DRF_response(data, status=status.HTTP_200_OK)
        except Scenarios.DoesNotExist:
            return DRF_response({'status': 'No scenario found for this scenario id'}, status=status.HTTP_404_NOT_FOUND)


class get_pages(APIView):
    def get(self, request, *args, **kwargs):

        scenario = self.request.query_params.get('scenario_id')

        try:
            scenario = Scenarios.objects.get(scenario_id=scenario)
        except Scenarios.DoesNotExist:
            return DRF_response(status=status.HTTP_404_NOT_FOUND)

        page_list = []
        page_id_list = PagesToScenario.objects.filter(scenario=scenario)

        for pg_id in page_id_list:
            try:
                page = Pages.objects.get(id=pg_id.page.id)
            except Pages.DoesNotExist:
                return DRF_response(status=status.HTTP_404_NOT_FOUND)
            page_list.append(page)

        sorted_list = []
        page_parent = {}
        for page in page_list:
            if page.next is not None:
                page_parent[str(page.next)] = page_parent.get(str(page.next), 0) + 1
            if page.page_type == 'A':
                action_pages = ActionPage.objects.filter(page = page.id)
                for action_page in action_pages:
                    try:
                        result_page = Pages.objects.get(id=action_page.result_page)
                        page_parent[str(result_page)] = page_parent.get(str(result_page), 0) + 1
                    except:
                        continue

        num_pages = len(page_list)

        for x in range(num_pages):
            page = None
            for page1 in page_list:
                if page_parent.get(str(page1), 0) <= 0:
                    page = page1
                    break
            if page is None:
                break
            page_serializer_data = PagesSerializer(page).data
            sorted_list.append(page_serializer_data)
            if page.next is not None:
                page_parent[str(page.next)] = page_parent.get(str(page.next), 0) - 1
            if page.page_type == 'A':
                action_pages = ActionPage.objects.filter(page = page.id)
                for action_page in action_pages:
                    try:
                        result_page = Pages.objects.get(id=action_page.result_page)
                        page_parent[str(result_page)] = page_parent.get(str(result_page), 0) - 1
                    except:
                        continue
            page_list.remove(page)

        def take_id(elem):
            return elem.id

        if len(page_list) > 0:
            page_list.sort(key=take_id)
            for page1 in page_list:
                page1 = PagesSerializer(page1).data
                if page1 not in sorted_list:
                    sorted_list.append(page1)
        results = {'results': sorted_list}
        return DRF_response(results, status=status.HTTP_200_OK)

class get_page_info(APIView):
    def get(self, request, *args, **kwargs):
        page_id = self.request.query_params.get('page_id')
    
        try:
            page = Pages.objects.get(id=page_id)
        except Pages.DoesNotExist:
            return DRF_response(status=status.HTTP_404_NOT_FOUND)
        page_data = PagesSerializer(page).data

        page_type = page.page_type
        # Check page.PAGE_TYPE = 'REFLECTION'
        if (page_type == 'R'):
            reflection_queries = ReflectionQuestionToPage.objects.filter(page=page_id)
            reflection_qs = []
            for quer in reflection_queries:
                try:
                    question = ReflectionQuestions.objects.get(id=quer.reflection_question.id)
                except:
                    return DRF_response(status=status.HTTP_404_NOT_FOUND)
                quer_data = Reflection_questionsSerializer(question).data
                reflection_qs.append(quer_data)
            page_data.update(
                {
                    "body": reflection_qs
                }
            )

        # Check page.PAGE_TYPE = 'ACTION'
        elif (page_type == 'A'):
            action_query = ActionPage.objects.filter(page=page_id).values()
            page_data.update(
                {
                    "body": action_query
                }
            )

        # Check page.PAGE_TYPE = 'GENERIC'
        elif (page_type == 'G' or page_type == 'I' or page_type == 'F'):
            generic_query = GenericPage.objects.filter(page=page_id).values()
            page_data.update(
                {
                    "body": generic_query
                }
            )

        # Check page.PAGE_TYPE = 'STAKEHOLDER'
        elif (page_type == 'S'):
            stakeholder_query = StakeholderToPage.objects.filter(page=page_id).values()
            page_data.update(
                {
                    "body": stakeholder_query
                }
            )
        # Neither of these pages, something went wrong or missing implementation
        else:
            return DRF_response(status=status.HTTP_400_BAD_REQUEST)

        return DRF_response(page_data, status=status.HTTP_200_OK)

class get_stakeholders(APIView):
    def get(self, request):
        scenario_id = self.request.query_params.get('scenario_id')
        try:
            scenario = Scenarios.objects.get(scenario_id=scenario_id)
        except Scenarios.DoesNotExist:
            return DRF_response(status=status.HTTP_404_NOT_FOUND)

        stakeholders_list = []
        stakeholders_id_list = Stakeholders.objects.filter(
            scenario_id=scenario_id)

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
            scenario = Scenarios.objects.get(scenario_id=scenario_id1)
        except Scenarios.DoesNotExist:
            return DRF_response(status=status.HTTP_404_NOT_FOUND)
        # serializer = IssueSerializer(scenario_id, many=True)
        # return DRF_response(serializer.data)
        if(scenario_id1 == None):
            return DRF_response(status=status.HTTP_400_BAD_REQUEST)
        try:
            issues_list = []
            AllIssues = Issues.objects.filter(scenario_id=scenario_id1)

            for issue in AllIssues:
                issue_data = IssueSerializer(issue).data
                issues_list.append(issue_data)
            # serializer = IssueSerializer(issues_list, many=True)
            return DRF_response(issues_list)
        except Issues.DoesNotExist:
            return DRF_response(status=status.HTTP_404_NOT_FOUND)



class issueRadarPlotTotal(APIView):

    def get(self, request, format=None):
        scenario_id = self.request.query_params.get('scenario_id')
        try:
            scenario = Scenarios.objects.get(scenario_id=scenario_id)
        except Scenarios.DoesNotExist:
            return DRF_response(status=status.HTTP_404_NOT_FOUND) 

        mp = {}
        try:
            stakeholder_list = Stakeholders.objects.filter(scenario = scenario_id)
            for stakeholder in stakeholder_list:
                stakeholder_id = stakeholder.id
                all_coverages = Coverage.objects.filter(stakeholder = stakeholder_id)
                for coverage in all_coverages:
                    issue = coverage.issue.name
                    score = coverage.coverage_score
                    mp[issue] = mp.get(issue, 0) + score

            return DRF_response(mp, status=status.HTTP_200_OK)
        except:
            return DRF_response(status=status.HTTP_400_BAD_REQUEST)


class issueScoreAggregateForStudent(APIView):

    def get(self, request, format=None):
        scenario_id1 = self.request.query_params.get('scenario_id')
        student_id = self.request.query_params.get('student_id')
        try:
            scenario = Scenarios.objects.get(scenario_id=scenario_id1)
        except Scenarios.DoesNotExist:
            return DRF_response(status=status.HTTP_404_NOT_FOUND)
        if(scenario_id1 == None):
            return DRF_response(status=status.HTTP_400_BAD_REQUEST)
        try:
            mp= {}
            AllResponses = Responses.objects.filter(student=student_id,scenario = scenario_id1) 
            stakeholderSet = set()
            for response in AllResponses:
                response_id = response.response_id
                responseToConvo = ResponsesToConversations.objects.filter(response=response_id)
                if len(responseToConvo) > 0:
                    for respToConv in responseToConvo:
                        stakeholderSet.add(respToConv.stakeholder.stakeholder)
            for stakeholder in stakeholderSet:
                coverages = Coverage.objects.filter(stakeholder=stakeholder)
                for coverage in coverages:
                    if coverage is not None:
                        issue_id = coverage.issue.name
                        coverage_score = coverage.coverage_score
                        mp[issue_id] = mp.get(issue_id, 0) + coverage_score
            return DRF_response(mp)
        except Scenarios.DoesNotExist:
            return DRF_response(status=status.HTTP_404_NOT_FOUND)



class response_to_conversations(APIView):
    def get(self, request):
        
        scenario_id = self.request.query_params.get('scenario_id')
        page_id  = self.request.query_params.get('page_id')
        student_id = self.request.query_params.get('student_id')
        
        try:
            scenario = Scenarios.objects.get(scenario_id = scenario_id)
            page = Pages.objects.get(page = page_id)
            student = Students.objects.get(student = student_id)
        except Scenarios.DoesNotExist:
            return rest_framework.response.Response(status=status.HTTP_404_NOT_FOUND)
        except Pages.DoesNotExist:
            return rest_framework.response.Response(status=status.HTTP_404_NOT_FOUND) 
        except Students.DoesNotExist:
            return rest_framework.response.Response(status=status.HTTP_404_NOT_FOUND)
        
        response_id_lst = Responses.objects.filter(student_id = student_id, page = page_id, scenario = scenario_id)
    
        resp_to_convo_final_lst = []
        for response in response_id_lst:
            resp_json = ResponseSerializer(response).data
            resp_to_convos_obj_lst = ResponsesToConversations.objects.filter(response_id = response.response_id)
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
        #     "student_id": "student netID",
        #     "conversation_id": 1,
        #     "score": 1,
        #     "course_id": 1,
        #     "page_id": 1
        # }

        scenario_id = request.data.get('scenario_id')
        student_id = request.data.get('student_id')
        conversation_id = request.data.get('conversation_id')
        # score = request.data.get('score')
        score = 0
        course_id = request.data.get('course_id')
        page_id = request.data.get('page_id')

        # extra check for if the given JSON has the required fields
        if(scenario_id is None or student_id is None or conversation_id is None or score is None or course_id is None or page_id is None):
            return DRF_response({'detail': "Missing one or more parameters"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            conversation = Conversations.objects.get(conversation=conversation_id)
            stakeholder_id = conversation.stakeholder.id
            stakeholder = Stakeholders.objects.get(id=stakeholder_id)
            scenario = Scenarios.objects.get(scenario_id=scenario_id)

            # Check if response is already in db
            try:
                responseObj = Responses.objects.get(response=0, student=student_id, scenario=scenario_id, page=page_id, course=course_id)
                responseSerializer = ResponseSerializer(responseObj)
            except:
                # formats the response entry to match the model if response does not exist
                response = {
                    "response": 0,
                    "student": student_id,
                    "scenario": scenario_id,
                    "page": page_id,
                    "version": 0,
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
                "stakeholder": stakeholder_id,
                "stakeholder_version": stakeholder.version,
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

            #increase version of response on success input
            responseObj = Responses.objects.get(response=0, student=student_id, scenario=scenario_id, page=page_id, course=course_id)
            responseObj.version = responseObj.version + 1
            response_instance = responseObj.save()
            return DRF_response(responseToConvSerializer.data, status=status.HTTP_200_OK)
        except:
            return DRF_response({'detail': "at least one parameter not found"}, status=status.HTTP_404_NOT_FOUND)

class start_scenario(APIView):
    def post(self, request, *args, **kwargs):
        scenario_id = self.request.query_params.get('scenario_id')
        student_id = self.request.query_params.get('student_id')
        course_id = self.request.query_params.get('course_id')
        
        try:
            scenario = Scenarios.objects.get(scenario_id = scenario_id)
            course = Courses.objects.get(course = course_id)
            student = Students.objects.get(student = student_id)
        except Scenarios.DoesNotExist:
            return DRF_response({'detail':"Scenario not found"}, status=status.HTTP_404_NOT_FOUND)
        except Students.DoesNotExist:
            return DRF_response({'detail':"Student not found"}, status=status.HTTP_404_NOT_FOUND)
        except Courses.DoesNotExist:
            return DRF_response({'detail':"Course not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            ScenariosFor.objects.get(scenario=scenario_id, course=course_id)
            StudentsToCourse.objects.get(student=student_id, course=course_id)
        except:
            return DRF_response({'detail': "Error in student to Scenario handling"}, status=status.HTTP_404_NOT_FOUND)
        
        try:
           studentTimeObj = StudentTimes.objects.get(student = student_id, course = course_id, scenario = scenario_id)
           return DRF_response({'detail': "scenario already started"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            stuTime = {
                "student": student_id,
                "course": course_id,
                "scenario": scenario_id,
                "page": -1,
                "end_time": None,
            }
            stutimeSerial = StudentTimesSerializer(data = stuTime)
            
            if not stutimeSerial.is_valid():
                return DRF_response(stutimeSerial.errors, status=status.HTTP_400_BAD_REQUEST)

            stutimeSerial.save()
            # return DRF_response(stuTime, status=status.HTTP_400_BAD_REQUEST)
            return DRF_response(stutimeSerial.data, status=status.HTTP_200_OK)
        

class current_page(APIView):
    def put(self, request, *args, **kwargs):
        scenario_id = self.request.query_params.get('scenario_id')
        student_id = self.request.query_params.get('student_id')
        course_id = self.request.query_params.get('course_id')
        page_id = self.request.query_params.get('page_id')
        
        try:
            scenario = Scenarios.objects.get(scenario_id = scenario_id)
            course = Courses.objects.get(course = course_id)
            student = Students.objects.get(student = student_id)
            page = Pages.objects.get(id = page_id)
        except Scenarios.DoesNotExist:
            return DRF_response({'detail':"Scenario not found"}, status=status.HTTP_404_NOT_FOUND)
        except Students.DoesNotExist:
            return DRF_response({'detail':"Student not found"}, status=status.HTTP_404_NOT_FOUND)
        except Courses.DoesNotExist:
            return DRF_response({'detail':"Course not found"}, status=status.HTTP_404_NOT_FOUND)
        except Pages.DoesNotExist:
            return rest_framework.response.Response({'detail':"Page not found"},status=status.HTTP_404_NOT_FOUND)
        try:
            ScenariosFor.objects.get(scenario=scenario_id, course=course_id)
            StudentsToCourse.objects.get(student=student_id, course=course_id)
        except:
            return DRF_response({'detail': "Error in student to Scenario handling"}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            PagesToScenario.objects.get(scenario=scenario_id, page=page_id)
        except PagesToScenario.DoesNotExist:
            return DRF_response({'detail': "The page is not in the current scenario"}, status=status.HTTP_404_NOT_FOUND)
        
        try:
           studentTimeObj = StudentTimes.objects.get(student = student_id, course = course_id, scenario = scenario_id)
           studentTimeObj.page = page_id
           studentTimeObj.save()
           stutimeSerial = StudentTimesSerializer(studentTimeObj)
           returnData = stutimeSerial.data
           return DRF_response(returnData)
        except StudentTimes.DoesNotExist:
            return DRF_response({'detail': "Student hasn't started Scenario"}, status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, *args, **kwargs):
        scenario_id = self.request.query_params.get('scenario_id')
        student_id = self.request.query_params.get('student_id')
        course_id = self.request.query_params.get('course_id')
        
        try:
            scenario = Scenarios.objects.get(scenario_id = scenario_id)
            course = Courses.objects.get(course = course_id)
            student = Students.objects.get(student = student_id)
        except Scenarios.DoesNotExist:
            return DRF_response({'detail':"Scenario not found"}, status=status.HTTP_404_NOT_FOUND)
        except Students.DoesNotExist:
            return DRF_response({'detail':"Student not found"}, status=status.HTTP_404_NOT_FOUND)
        except Courses.DoesNotExist:
            return DRF_response({'detail':"Course not found"}, status=status.HTTP_404_NOT_FOUND)
        try:
            ScenariosFor.objects.get(scenario=scenario_id, course=course_id)
            StudentsToCourse.objects.get(student=student_id, course=course_id)
        except:
            return DRF_response({'detail': "Error in student to Scenario handling"}, status=status.HTTP_404_NOT_FOUND)
        
        try:
           studentTimeObj = StudentTimes.objects.get(student = student_id, course = course_id, scenario = scenario_id)
           stutimeSerial = StudentTimesSerializer(studentTimeObj)
           returnData = stutimeSerial.data
           return DRF_response(returnData)
        except StudentTimes.DoesNotExist:
            return DRF_response({'detail': "Student hasn't started Scenario"}, status=status.HTTP_404_NOT_FOUND)
        

class student_finish_scenario(APIView):
    def get(self, request, *args, **kwargs):
        scenario_id = self.request.query_params.get('scenario_id')
        student_id = self.request.query_params.get('student_id')
        course_id = self.request.query_params.get('course_id')
        
        try:
            scenario = Scenarios.objects.get(scenario_id = scenario_id)
            course = Courses.objects.get(course = course_id)
            student = Students.objects.get(student = student_id)
        except Scenarios.DoesNotExist:
            return DRF_response({'detail':"Scenario not found"}, status=status.HTTP_404_NOT_FOUND)
        except Students.DoesNotExist:
            return DRF_response({'detail':"Student not found"}, status=status.HTTP_404_NOT_FOUND)
        except Courses.DoesNotExist:
            return DRF_response({'detail':"Course not found"}, status=status.HTTP_404_NOT_FOUND)
        try:
            ScenariosFor.objects.get(scenario=scenario_id, course=course_id)
            StudentsToCourse.objects.get(student=student_id, course=course_id)
        except:
            return DRF_response({'detail': "Error in student to Scenario handling"}, status=status.HTTP_404_NOT_FOUND)
        
        try:
           studentTimeObj = StudentTimes.objects.get(student = student_id, course = course_id, scenario = scenario_id)
           stutimeSerial = StudentTimesSerializer(studentTimeObj)
           if (studentTimeObj.end_time is None):
               return DRF_response({'finished': False}, status=status.HTTP_200_OK)
           return DRF_response({'finished': True}, status=status.HTTP_200_OK)
        except StudentTimes.DoesNotExist:
            return DRF_response({'detail': "Student hasn't started Scenario", 'finished': False}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        scenario_id = self.request.query_params.get('scenario_id')
        student_id = self.request.query_params.get('student_id')
        course_id = self.request.query_params.get('course_id')
        
        try:
            scenario = Scenarios.objects.get(scenario_id = scenario_id)
            course = Courses.objects.get(course = course_id)
            student = Students.objects.get(student = student_id)
        except Scenarios.DoesNotExist:
            return DRF_response({'detail':"Scenario not found"}, status=status.HTTP_404_NOT_FOUND)
        except Students.DoesNotExist:
            return DRF_response({'detail':"Student not found"}, status=status.HTTP_404_NOT_FOUND)
        except Courses.DoesNotExist:
            return DRF_response({'detail':"Course not found"}, status=status.HTTP_404_NOT_FOUND)
        try:
            ScenariosFor.objects.get(scenario=scenario_id, course=course_id)
            StudentsToCourse.objects.get(student=student_id, course=course_id)
        except:
            return DRF_response({'detail': "Error in student to Scenario handling"}, status=status.HTTP_404_NOT_FOUND)
        
        try:
           studentTimeObj = StudentTimes.objects.get(student = student_id, course = course_id, scenario = scenario_id)
           studentTimeObj.end_time = datetime.date.today()
           studentTimeObj.save()
           stutimeSerial = StudentTimesSerializer(studentTimeObj)
           returnData = stutimeSerial.data
           return DRF_response(returnData)
        except StudentTimes.DoesNotExist:
            return DRF_response({'detail': "Student hasn't started Scenario"}, status=status.HTTP_404_NOT_FOUND)

class reflection(APIView):
    #retrieve a reflection for a particular response from the database
    def get(self, request, *args, **kwargs):
        page_id = self.request.query_params.get('page_id') 
        student_id = self.request.query_params.get('student_id')
        scenario_id = self.request.query_params.get('scenario_id')


        # extra check for if the given JSON has the required fields
        if(scenario_id is None or page_id is None or student_id is None ):
            return DRF_response({'detail': "Missing one or more parameters"}, status=status.HTTP_400_BAD_REQUEST)

        responses = Responses.objects.filter(page= page_id, student = student_id, scenario = scenario_id)
        if len(responses) <= 0:
            return DRF_response({"detail": "Response does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            reflections = []
            for responseObj in responses:
                ref = ReflectionsTaken.objects.filter(response = responseObj.response_id).first()
                reflection_data = ReflectionsTakenSerializer(ref).data
                reflection_data['response_id'] = responseObj.response_id
                reflection_data['response'] = responseObj.response
                reflections.append(reflection_data)
            return DRF_response(reflections, status.HTTP_200_OK)
        except ReflectionsTaken.DoesNotExist:
            return DRF_response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        page_id = self.request.query_params.get('page_id') 
        student_id = self.request.query_params.get('student_id')
        scenario_id = self.request.query_params.get('scenario_id')
        # reflections = self.request.query_params.get('reflections')
        reflections = request.data.get('reflection')
        response = request.data.get('response')

        # extra check for if the given JSON has the required fields
        if(scenario_id is None or page_id is None or student_id is None or reflections is None or response is None):
            return DRF_response({'detail': "Missing one or more parameters"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            responseObj = Responses.objects.filter(response=response, page= page_id, student = student_id, scenario = scenario_id).first()
            if responseObj is not None:
                ref = ReflectionsTaken.objects.filter(response = responseObj.response_id).first()
                if ref is not None:
                    ref.reflections = reflections
                    serializer = ReflectionsTakenSerializer(ref)
                    ref.save()
                    return DRF_response(serializer.data)

                return self.post(request)
        except Responses.DoesNotExist:
            return DRF_response(status=status.HTTP_404_NOT_FOUND)
        except:
            return DRF_response(status=status.HTTP_400_BAD_REQUEST)
            """       
            if response is None:
                serializer = ResponseSerializer(data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                response = Responses.objects.filter(page= page_id, student = student_id, scenario = scenario_id).first()
            ReflectionsTaken.objects.create(response=response,reflection=reflections)
            ref = ReflectionsTaken.objects.filter(response = response.response_id).first()
            serializer = ReflectionsTakenSerializer(ref)
            return DRF_response(serializer.data)
            """

    def post(self, request):
        page_id = self.request.query_params.get('page_id') 
        student_id = self.request.query_params.get('student_id')
        scenario_id = self.request.query_params.get('scenario_id')
        # reflections = self.request.query_params.get('reflections')
        reflections = request.data.get('reflection')
        response = request.data.get('response')
        
        responses = Responses.objects.filter(response=response, page= page_id, student = student_id, scenario = scenario_id)
        if(len(responses) > 0):
            return self.put(request)

        serializer = ResponseSerializer(data=request.data)
        response_instance = None
        if serializer.is_valid():
            response_instance = serializer.save()
        else:
            return DRF_response({"detail": "cannot create response"}, status=status.HTTP_400_BAD_REQUEST)
        responseObj = Responses.objects.filter(response=response, page= page_id, student = student_id, scenario = scenario_id).first()
        newref={
                "response":responseObj.response_id,
                "reflections":reflections
            }
        serializer = ReflectionsTakenSerializer(data=newref)
        if serializer.is_valid():
            serializer.save()
            return DRF_response(serializer.data)
        response_instance.delete()
        return DRF_response(status=status.HTTP_400_BAD_REQUEST)


class stakeholder_conv(APIView):
    def get(self, request, *args, **kwargs):
        stakeholder_id = self.request.query_params.get('stakeholder_id')

        if(stakeholder_id is None):
            return DRF_response({'detail': "Missing parameter: stakeholder_id"}, status=status.HTTP_400_BAD_REQUEST)
        
        conversations_list = []
        try:
            conversations = Conversations.objects.filter(stakeholder=stakeholder_id)
            for conversation in conversations:
                conversation_data = ConversationSerializer(conversation).data
                conversations_list.append(conversation_data)
            return DRF_response(conversations_list, status=status.HTTP_200_OK)
        except Conversations.DoesNotExist:
            return DRF_response(status=status.HTTP_404_NOT_FOUND)

class response_to_action_page(APIView):
    def get(self, request, *args, **kwargs):
        student_id = self.request.query_params.get('student_id')
        page_id = self.request.query_params.get('page_id')
        scenario_id = self.request.query_params.get('scenario_id')

        if(student_id is None or page_id is None or scenario_id is None):
            return DRF_response({'detail': "Missing parameter: stakeholder_id"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            action_pages = ActionPage.objects.filter(page=page_id)
            response = Responses.objects.filter(student_id = student_id, page = page_id, scenario=scenario_id).first()
            for action_page in action_pages:
                action_page_id = action_page.id
                response_to_action = ResponseToActionPage.objects.filter(response=response, action_page=action_page_id)
                if(len(response_to_action) > 0):
                    action_page = ActionPage.objects.get(id = action_page_id)
                    action_page_serializer = Action_pageSerializer(action_page)
                    return DRF_response(action_page_serializer.data, status=status.HTTP_200_OK)
            return DRF_response({"detail": "No action response entry found."}, status=status.HTTP_404_NOT_FOUND)
        except:
            return DRF_response({"detail": "unknown error"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        action_page_id0 = self.request.query_params.get('action_page_id') 
        student_id = self.request.query_params.get('student_id')
        scenario_id = self.request.query_params.get('scenario_id')
        course_id = self.request.query_params.get('course_id')

        if(scenario_id is None or student_id is None or action_page_id0 is None or course_id is None):
            return DRF_response({'detail': "Missing one or more parameters"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            action_page = ActionPage.objects.get(id = action_page_id0)
        except ActionPage.DoesNotExist:
            return DRF_response({"detail": "action id not found"}, status=status.HTTP_404_NOT_FOUND)
           
        try:
            response0 = Responses.objects.get(response=0, scenario = scenario_id, student = student_id, course = course_id, page=action_page.page)
            # responseSerializer = ResponseSerializer(response0)
            return DRF_response({"detail": "The player already made an action choice on this page!"}, status=status.HTTP_400_BAD_REQUEST)
        except Responses.DoesNotExist:
            response0 = {
                    "response": 0,
                    "student": student_id,
                    "scenario": scenario_id,
                    "page": action_page.page.id,
                    "version": 0,
                    "course": course_id,
                    "choice": str(action_page_id0)
                }
            responseSerializer = ResponseSerializer(data = response0)

            if not responseSerializer.is_valid():
                return DRF_response(responseSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
            responseSerializer.save()

        resp_to_action = {
                "response": responseSerializer.data['response_id'],
                "action_page": action_page_id0
            }
           
        resp_to_action_serializer = ResponseToActionPageSerializer(data=resp_to_action)
        
        if not resp_to_action_serializer.is_valid():
            return DRF_response(resp_to_action_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        resp_to_action_serializer.save()

        return DRF_response(resp_to_action_serializer.data, status=status.HTTP_200_OK)


class stakeholders_had(APIView):
    def get(self, request):
        scenario_id1 = self.request.query_params.get('scenario_id')
        student_id = self.request.query_params.get('student_id')
        try:
            scenario = Scenarios.objects.get(scenario_id=scenario_id1)
        except Scenarios.DoesNotExist:
            return DRF_response(status=status.HTTP_404_NOT_FOUND)
        if(scenario_id1 == None):
            return DRF_response(status=status.HTTP_400_BAD_REQUEST)

        try:
            AllResponses = Responses.objects.filter(student=student_id,scenario = scenario_id1) 
            stakeholderSet = set()
            for response in AllResponses:
                response_id = response.response_id
                responseToConvo = ResponsesToConversations.objects.filter(response=response_id)
                if len(responseToConvo) > 0:
                    for respToConv in responseToConvo:
                        stakeholderSet.add(respToConv.stakeholder)
            result = []
            for stakeholder in stakeholderSet:
                result.append(StakeholderSerializer(stakeholder).data['id'])
            return DRF_response(result)
        except Scenarios.DoesNotExist:
            return DRF_response(status=status.HTTP_404_NOT_FOUND)