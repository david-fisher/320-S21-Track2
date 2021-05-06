from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializer import *
from django.core import serializers
from rest_framework import status  
import json
from django.db import connection
from rest_framework.parsers import JSONParser
from rest_framework.viewsets import ModelViewSet
from django.http.response import JsonResponse
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from rest_framework import mixins
# DemographicsSerializer, StudentSerializer, ProfessorSerializer, ScenariosSerializer, allScenariosSerializer, Stakeholder_pageSerializer, StakeholdersSerializer, ConversationsSerializer


def getcredentials(request):
    credentials = {
        "uid": request.meta['uid'],
        "name": request.meta['displayname'],
        "affiliation": request.meta['edupersonprimaryaffiliation'],
        "email": request.meta['mail'],
        #"title": request.meta['title'],
        "intid": request.meta['fcidnumber']
    }
    credentials.update({"intid": credentials.get("intid").split("@")[0]})
    return credentials


class ReturnIdentifierView(APIView):
    def get(self, request, *args, **kwargs):
        if ('title' in request.meta):
            return Response({"id":"professor"})
        else:
            # if(len(scenarios.objects.filter(professors_to_scenario = request.meta['displayname']).values()) != 0):
            #     return Response({"id":"editor"})
            # else:
            return Response({"id":"student"})

        # if (credentials.get("title") == "lecturer"):
        #     return Response({"id":"professor"})
        # else:
        #     return Response({"id":"student"})
        #return Response({"id":"student"})


# stakeholders viewset - chirag - 4/14
class StakeholdersViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = stakeholders.objects.all()
        return queryset
    queryset = stakeholders.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = StakeholdersSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['scenario']
    lookup_field = 'stakeholder'

# class stakeholdersviewset(viewsets.ModelViewSet):
#     queryset = stakeholders.objects.all()
#     permissions_classes = [
#         permissions.AllowAny
#     ]
#     serializer_class = stakeholdersserializer

class QuestionsViewset(viewsets.ModelViewSet):
    queryset = questions.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = QuestionsSerializer

# conversations viewset
# checked - chirag - 04/15/2021
class ConversationsViewSet(viewsets.ModelViewSet):
    queryset = conversations.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = ConversationsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['stakeholder', 'question']

class Responses_to_ConversationsViewSet(viewsets.ModelViewSet):
    queryset = responses_to_conversations.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = Responses_to_ConversationsSerializer

# checked - chirag - 04/15/2021
class multi_conv(APIView):
    def put(self, request, *args, **kwargs):
        stakeholder = self.request.query_params.get('stakeholder')
        if stakeholder == None:
            return Response({'status': 'details'}, status=status.HTTP_404_NOT_FOUND)
        for updated_conv in request.data:
            extant_conv = conversations.objects.get(stakeholder = stakeholder, conversation = updated_conv['conversation'])
            serializer = ConversationsSerializer(extant_conv, data=updated_conv)
            if serializer.is_valid(): 
                serializer.save()
        conv_query = conversations.objects.filter(stakeholder = stakeholder).values()
        return Response(conv_query)

# no change - checked - chirag - 04/15/2021
class multi_stake(APIView):
    def put(self, request, *args, **kwargs):
        scenario = self.request.query_params.get('scenario')
        if scenario == None:
            return Response({'status': 'details'}, status=status.HTTP_404_NOT_FOUND)
        for updated_stake in request.data:
            extant_stake = stakeholders.objects.get(scenario_id = scenario, stakeholder = updated_stake['stakeholder'])
            serializer = StakeholdersSerializer(extant_stake, data=updated_stake)
            if serializer.is_valid():
                serializer.save()
        stake_query = stakeholders.objects.filter(scenario = scenario).values()
        return Response(stake_query)

# checked - ed - 4/15/2021
class multi_coverage(APIView):
    def put(self, request, *args, **kwargs):
        stakeholder = self.request.query_params.get('stakeholder')
        if stakeholder == None:
            return Response({'status': 'details'}, status=status.HTTP_404_NOT_FOUND)
        for updated_coverage in request.data:
            extant_coverage = coverage.objects.get(stakeholder = stakeholder, issue = updated_coverage['issue_id'])
            serializer = coverageSerializer(extant_coverage, data=updated_coverage)
            if serializer.is_valid():
                serializer.save()
        coverage_query = coverage.objects.filter(stakeholder = stakeholder).values()
        return Response(coverage_query)


# done - chirag - 04/15/2021
class CoverageViewSet(viewsets.ModelViewSet):
    queryset = coverage.objects.all()
    permission_classe = [permissions.AllowAny]
    serializer_class = coverageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['stakeholder']

    

class DemographicsViewSet(viewsets.ModelViewSet):
    queryset = demographics.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DemographicsSerializer

class StudentsViewSet(viewsets.ModelViewSet):
    queryset = students.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StudentSerializer

class PagesToScenarioViewSet(viewsets.ModelViewSet):
    queryset = pages_to_scenario.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PagesToScenarioSerializer

class ProfessorsViewSet(viewsets.ModelViewSet):
    queryset = professors.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProfessorSerializer

class StudentTimesViewSet(viewsets.ModelViewSet):
    queryset = student_times.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StudentTimesSerializer


class ScenariosViewSet(viewsets.ModelViewSet):
    queryset = scenarios.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = ScenariosSerializer

    # uncommeented cuz main - chirag - 04/15/2021
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SingleScenarioViewSet(viewsets.ModelViewSet):
    def get(self, request):
        scenario = scenarios.objects.all()
        serializer = ScenariosSerializer(scenarios)
        return Response(serializer.data)

# class professors_to_scenarioviewset(viewsets.ModelViewSet):
#     def get(self, request):
#         scenario = scenarios.objects.all()
#         serializer = scenariosserializer(scenarios)
#         return Response(serializer.data)
    
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class professors_to_scenarioViewSet(viewsets.ModelViewSet):
    queryset = professors_to_scenario.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = Professors_to_scenarioSerializer

class PagesViewSet(viewsets.ModelViewSet):
    queryset = pages.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = PagesSerializer

# stakeholder_page viewset
class Stakeholder_pageViewSet(viewsets.ModelViewSet):
    queryset = stakeholder_to_page.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = Stakeholder_to_pageSerializer


class Reflection_QuestionsViewSet(viewsets.ModelViewSet):
    queryset = reflection_questions.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = Reflection_questionsSerializer

class Reflection_Question_to_pageViewSet(viewsets.ModelViewSet):
    queryset = reflection_question_to_page.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = Reflection_questions_to_pageSerializer

class ReflectionsTakenViewSet(viewsets.ModelViewSet):
    queryset = reflections_taken.objects.all()
    permission_class = [
        permissions.AllowAny
    ]
    serializer_class = ReflectionsTakenSerializer

# class actionstakenviewset(viewsets.ModelViewSet):
#     queryset = actions_taken.objects.all()
#     permission_class = [
#         permissions.AllowAny
#     ]
#     serializer_class = actions_takenserializer
# class conversationshadviewset(viewsets.ModelViewSet):
#     queryset = conversations_had.objects.all()
#     permission_class = [
#         permissions.AllowAny
#     ]
#     serializer_class = conversationshadserializer


# class studentsinviewset(viewsets.ModelViewSet):
#     queryset = students_in.objects.all()
#     permission_class = [permissions.AllowAny]
#     serializer_class = studentsinserializer


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = courses.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CoursesSerializer


class ResponsesViewSet(viewsets.ModelViewSet):
    queryset = responses.objects.all()
    permission_classe = [permissions.AllowAny]
    serializer_class = ResponsesSerializer

#this allows for filerting scenarios by professor_id
class allScenariosViewSet(generics.ListAPIView):
    serializer_class = allScenariosSerializer
    queryset = scenarios.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['professor', 'is_finished']
    
# scenarios_for viewset
class Scenarios_forViewSet(viewsets.ModelViewSet):
    queryset = scenarios_for.objects.all()
    permissions_class = [
        permissions.AllowAny
    ]
    serializer_class = Scenarios_forSerializer

class courses_to_scenarioViewset(viewsets.ModelViewSet):
    queryset = courses_to_scenario.objects.all()
    permissions_class = [
        permissions.AllowAny
    ]
    serializer_class = Courses_to_ScenarioSerializer

# generic_page viewset
class generic_pageViewSet(viewsets.ModelViewSet):
    queryset = generic_page.objects.all()
    permissions_class = [
        permissions.AllowAny
    ]
    serializer_class = Generic_pageSerializer

# professors_teach viewset
# class professors_teachviewset(viewsets.ModelViewSet):
#     queryset = professors_teach.objects.all()
#     permissions_class = [
#         permissions.AllowAny
#     ]
#     serializer_class = professors_teachserializer

# changed - chirag - 04/15/2021
class IssuesViewSet(viewsets.ModelViewSet):
    queryset = issues.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = IssuesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['scenario_id', "name"]


class Action_pageViewSet(viewsets.ModelViewSet):
    queryset = action_page.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = Action_pageSerializer

class response_to_action_pageViewSet(viewsets.ModelViewSet):
    queryset = response_to_action_page.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = Response_to_action_pageSerializer


# checked - ed - 4/15/21
#for getting/editing scenarios in dashboard
class logistics_page(APIView):
    #http_method_names = [ 'post,' 'put', 'delete']

    def get(self, request, *args, **kwargs):
        
        #take professor_id as input from url by adding ?professor_id=<the id #> to the end of the url.
        scenario_id = self.request.query_params.get('scenario')
        #todo check that id != None
        #get all scenarios belonging to this professor
        # scenario_query = professors_to_scenario.objects.filter(professor = professor_id).values()
        scenario = scenarios.objects.get(scenario_id = scenario_id)
        scenario_dict = scenariosserializer(scenario).data
        #loop through scenarios and append required information (course, page info)
        # print(scenario_dict)
        scenarios_for_query = scenarios_for.objects.filter(scenario_id=scenario_dict['scenario_id']).values()
        course_id_array = []
        for x in scenarios_for_query:
            # print(x)
            course_id_array.append(x['course'])

        course_dict_array = []
        for x in course_id_array:
            course = courses.objects.get(course = x)
            course_dict_array.append({"course":course.course, "name": course.name})
                
        pages_query = pages.objects.filter(scenario=scenario_id).values()
        # print("pages: ", pages_query)
        page_array = []
        for page in pages_query:
            cropped_page = {}
            cropped_page['page'] = page['page']
            cropped_page['page_title'] = page['page_title']
            cropped_page['page_type'] = page['page_type']
            page_array.append(cropped_page) 


        scenario_dict.update({
            "courses": course_dict_array,
            "pages": page_array
        })

        
        logistics = scenario_dict
        # print(logistics)
        return Response(logistics)
    
    """format:
    {
        "scenario": 1,
        "version": 0,
        "name": "pizza is good!",
        "is_finished": false,
        "public": false,
        "num_conversation": 5,
        "professor": 12345678,
        "courses": 
        [
            {
                "course": 2,
                "name": "590g"
            },
            {
                "course": 1,
                "name": "320"
            }
        ]
    }
        """
    #a put request for editing scenarios. must provide scenario in url thusly: /logistics?scenario=<insert id number here>
    def put(self, request, *args, **kwargs):
        #save the scenario
        extant_scenario = scenarios.objects.get(scenario_id = request.data['scenario_id'])
        scenario_serializer = ScenariosSerializer(extant_scenario, data = request.data)
        if scenario_serializer.is_valid():
            scenario_serializer.save()

        #delete currently assocated classes
        scenarios_for.objects.filter(scenario_id = request.data['scenario_id']).delete()
        #get array of courses from frontend
        courses = request.data['courses']
        for course in courses:
            scenarios_for_dict = {
                "course" : course['course'],
                "scenario" : request.data['scenario'],
                "version" : request.data['version']
            }
            print(scenarios_for_dict)
        #save the classes associated with it in scenarios_for
            for_serializer = Scenarios_forSerializer(data=scenarios_for_dict)
            if for_serializer.is_valid():
                for_serializer.save()
                print('saved!')
            print(for_serializer.errors)
        scenario_dict = ScenariosSerializer(scenarios.objects.get(scenario_id = request.data['scenario_id'])).data
        scenario_dict['courses'] = request.data['courses']
        return Response(scenario_dict)

# checked - ed - 4/15/2021
#returns list of scenarios for given professor along with list of associated courses
class dashboard_page(APIView):
    def get(self, request, *args, **kwargs):
        
        #take professor_id as input from url by adding ?professor=<the id #> to the end of the url.
        
        #--old schema
        #professor_id = self.request.query_params.get('professor')
        
        #new, changed the endpoint request
        professor_id = request.META['uid']
        #todo check that id != None
        #get all scenarios belonging to this professor
        scenario_query = scenarios.objects.filter(pts2 = professor_id).values()
        if(len(scenario_query) == 0):
            return Response({"error": "you are not associated with any scenarios"})
        #loop through scenarios and append required information (course, page info)
        logistics = []
        print(scenario_query)
        for scenario in scenario_query:
            scenarios_for_query = scenarios_for.objects.filter(scenario_id = scenario['scenario']).values()
            course_id_array = []
            for x in scenarios_for_query:
                course_id_array.append(x['course'])

            course_dict_array = []
            for x in course_id_array:
                course = courses.objects.get(course= x)
                course_dict = {"course":course.course, "name": course.name}
                course_dict_array.append(course_dict)
                    
            scenario["courses"] = course_dict_array
            logistics.append(scenario)
                
        return Response(logistics)

        """format:

        {
        "name": "best test",
        "is_finished": false,
        "public": false,
        "num_conversation": 5,
        "professor": 12345678,
        "courses":[
            {"course": 1},
            {"course": 2},
            {"course": 3}
        ]
        }
        """

    def post(self, request, *args, **kwargs):
        #save the scenario
        scenario_serializer = ScenariosSerializer(data = request.data)
        if not (scenario_serializer.is_valid()):
            print("scenario saved incorrectly")
            return Response(scenario_serializer.errors)
        scenario_serializer.save()
        scenario_dict = scenario_serializer.data
        
        #get array of courses from frontend
        courses = request.data['courses']
        for course in courses:
            scenarios_for_dict = {
                "scenario" : scenario_dict['scenario'],
                "course" : course['course'],
                "version" : scenario_dict['version']
            }
            print(scenarios_for_dict)
            print(scenario_dict)
            for_serializer = Scenarios_forSerializer(data=scenarios_for_dict)
            if not for_serializer.is_valid():
                print("scenarios_for saved incorrectly")
                return Response(for_serializer.errors)

            for_serializer.save()

        #create a new intro page
        intro_page = {
        "page_type": "i",
        "page_title": "introduction",
        "page_body": "page body",
        "scenario": scenario_dict['scenario'],
        "next_page": None,
        "x_coordinate": 0,
        "y_coordinate": 0,
        "next_page_version": None
        }

        intro_page_serializer = PagesSerializer(data=intro_page)
        if intro_page_serializer.is_valid():
            intro_page_serializer.save()
            print("intro page saved")
        else:
            print("intro page saved incorrectly")
            return Response(intro_page_serializer.errors)

        #todo create blank stakeholder page and return it
        #page must be called stakeholder_page and serialier must be called stakeholder_page_serializer
        stakeholder_page = {
        "page_type": "s",
        "page_title": "stakeholders",
        "page_body": "page of stakeholders",
        "scenario": scenario_dict['scenario'],
        "next_page": None,
        "x_coordinate": 0,
        "y_coordinate": 0,
        "next_page_version": None
        }

        stakeholder_page_serializer = PagesSerializer(data=stakeholder_page)
        if stakeholder_page_serializer.is_valid():
            stakeholder_page_serializer.save()
        else:
            print("stakeholders page saved incorrectly")
            return Response(stakeholder_page_serializer.errors)


        scenario_dict = ScenariosSerializer(scenarios.objects.get(scenario = scenario_dict['scenario'])).data
        scenario_dict['courses'] = request.data['courses']
        scenario_dict['intro_page'] = intro_page_serializer.data
        scenario_dict['stakeholder_page'] = stakeholder_page_serializer.data
        return Response(scenario_dict)

     
# checked - ed - 4/15/2021
#change a list of issue objects at url /multi_issue?scenario=<insert id number here>
class multi_issue(APIView):
    def put(self, request, *args, **kwargs):
        scenario = self.request.query_params.get('scenario')
        if scenario == None:
            return Response({'status': 'details'}, status=status.HTTP_404_NOT_FOUND)
        for updated_issue in request.data:
            extant_issue = issues.objects.get(scenario_id = scenario, issue = updated_issue['issue'])
            serializer = IssuesSerializer(extant_issue, data=updated_issue)
            if not serializer.is_valid(): 
                return Response(serializer.errors)
            try:
                serializer.save()
            except:
                print('something went wrong with the put')
        issues_query = issues.objects.filter(scenario_id = scenario).values()
        return Response(issues_query)

# checked - ed - 4/15/2021
#for use in the pages flowchart, input is an array of page objects
class flowchart(APIView):
    #get all page objects given a scenario id
    def get(self, request, *args, **kwargs):
        scenario_id = self.request.query_params.get('scenario')
        print(scenario_id)
        pages_query = pages.objects.filter(scenario=scenario_id).values()
        print(pages_query)
        for page in pages_query:
            if page['page_type'] == 'a':
                page['action'] = action_page.objects.filter(page=page['page']).values()


        return Response(pages_query)

    #update the next_page field of all page objects
    def put(self, request, *args, **kwargs):
        scenario_id = self.request.query_params.get('scenario')
        if scenario_id == None:
            return Response({'status': 'details'}, status=status.HTTP_404_NOT_FOUND)
  
        for updated_page in request.data:
            #save updated choices within action pages  
            if updated_page['page_type'] == 'a':
                print('action page')
                print(update)
                for updated_choice in updated_page['action']:
                    print(updated_choice)
                    extant_choice = action_page.objects.get(id=updated_choice['id']) 
                    action_serializer = action_pageserializer(extant_choice, updated_choice)
                    if not action_serializer.is_valid():
                        print("error with puting choices")
                        return Response(action_serializer.errors)
                    action_serializer.save()
            #save the page itself    
            extant_page = pages.objects.get(scenario = scenario_id, page = updated_page['page'])
            serializer = PagesSerializer(extant_page, data=updated_page)
            if not serializer.is_valid():
                print("error with puting pages")
                return Response(serializer.errors)
            serializer.save()
        #return query with newly saved pages     
        pages_query = pages.objects.filter(scenario=scenario_id).values()
        for page in pages_query:
            if page['page_type'] == 'a':
                page['action'] = action_page.objects.filter(page=page['page']).values()
        return Response(pages_query)



#pages viewset
#Cooper 05/05/2021
class Page_reflectionViewSet(generics.CreateAPIView):
    model = pages
    serializer_class = Pages_reflectionSerializer

#Cooper 05/05/2021
class Page_actionViewSet(generics.CreateAPIView):
    model = pages
    serializer_class = Pages_actionSerializer  

#Cooper 05/05/2021
class Page_genericViewSet(generics.CreateAPIView):
    model = pages
    serializer_class = Pages_genericSerializer

#Cooper 05/05/2021
class Page_StakeholderViewSet(generics.CreateAPIView):
    model = pages
    serializer_class = Pages_stakeholderSerializer
    


class pages_page(APIView):
    # define get method for pages
    # @api_view(['get'])
    def get(self, request, *args, **kwargs):

        # takes the page_id from the url if the url has ?page_id=<id> at the end, no parameter passed return error 400
        page_id = self.request.query_params.get('page_id')

        # get all fields from this page_id if ti doesn't exist return error 404
        try:
            page = pages.objects.get(page = page_id)
        except pages.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        # print(page)
        # convers django model object into a dictionary
        page_data = PagesSerializer(page).data
        # print(page_data)
        page_type = page_data['page_type']
        # print("page type: ", page_type)
        # check page.page_type = 'reflection'
        if (page_type == 'r'):
            reflection_query = reflection_questions.objects.filter(reflection_questions_to_page1 = page_id).values()
            page_data.update(
                {
                    "reflection_questions": reflection_query
                }
            )
            
            return Response(page_data, status=status.HTTP_200_OK)

        # check page.page_type = 'action'
        if (page_type == 'a'):
            action_query = action_page.objects.filter(page = page_id).values()
            page_data.update(
                {
                    "choices": action_query
                }
            )

            return Response(page_data, status=status.HTTP_200_OK)
        
        # check page.page_type = 'generic'
        if (page_type == 'g' or page_type == 'i'):
            generic_query = generic_page.objects.filter(page = page_id).values()
            page_data.update(
                {
                    "bodies":generic_query
                }
            )

            return Response(page_data, status=status.HTTP_200_OK)
        
        # check page.page_type = 'stakeholder'
        if (page_type == 's'):
            stakeholder_query = stakeholder_to_page.objects.filter(page = page_id).values()
            page_data.update(
                {
                    "stakeholders": stakeholder_query
                }
            )

            return Response(page_data, status=status.HTTP_200_OK)
        
        # neither of these pages, something went wrong or missing implementation
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
#     # define post function for pages
#     # @api_view(['post'])
    def post(self, request):

        # takes the scenario_id from the url if the url has ?scenario_id=<id> at the end, no parameter passed return error 400

        page_type = request.data["page_type"]

        # if the request is a reflection page  
        if (page_type == 'r'):
            pages_serializer = PagesSerializer(data=request.data)
            if pages_serializer.is_valid():
                pages_serializer.save()
                page_id = pages_serializer.data["page"]
                for question in request.data['reflection_questions']:
                    question['page'] = page_id
                    nested_serializer = Reflection_questionsSerializer(data=question)
                    if  nested_serializer.is_valid():
                        nested_serializer.save()
                    # if the nested page is not valid it deletes the wrapper page created above
                    else:
                        page = pages.objects.get(page=page_id)
                        page.delete()
                        return Response(nested_serializer.data, status=status.HTTP_400_BAD_REQUEST)
                    #nested_serializer.save()
                return Response(pages_serializer.data, status=status.HTTP_201_CREATED)
            
            # if the request was badly made or could not be created
            return Response(pages_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # if the request is an action page  
        if (page_type == 'a'):
            pages_serializer = PagesSerializer(data=request.data)
            if pages_serializer.is_valid():
                pages_serializer.save()
                page_id = pages_serializer.data["page"]
                for choice in request.data['page_choices']:
                    choice['page'] = page_id
                    nested_serializer = Action_pageSerializer(data=choice)
                    if  nested_serializer.is_valid():
                        nested_serializer.save()
                    # if the nested page is not valid it deletes the wrapper page created above
                    else:
                        page = pages.objects.get(page=page_id)
                        page.delete()
                        return Response(nested_serializer.data, status=status.HTTP_400_BAD_REQUEST)
                    #nested_serializer.save()
                return Response(pages_serializer.data, status=status.HTTP_201_CREATED)
            
            # if the request was badly made or could not be created
            return Response(pages_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        # if the request is a generic page  
        if (page_type == 'g' or page_type == 'i'):
            pages_serializer = PagesSerializer(data=request.data)
            if pages_serializer.is_valid():
                pages_serializer.save()
                page_id = pages_serializer.data["page"]
                for body in request.data['body']:
                    body['page'] = page_id
                    nested_serializer = Generic_pageSerializer(data=body)
                    if  nested_serializer.is_valid():
                        nested_serializer.save()
                    # if the nested page is not valid it deletes the wrapper page created above
                    else:
                        page = pages.objects.get(page=page_id)
                        page.delete()
                        return Response(nested_serializer.data, status=status.HTTP_400_BAD_REQUEST)
                    #nested_serializer.save()
                return Response(pages_serializer.data, status=status.HTTP_201_CREATED)
            
            # if the request was badly made or could not be created
            return Response(pages_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # if the request is a stakeholder page 
        if (page_type == 's'):
            pages_serializer = PagesSerializer(data=request.data)
            if pages_serializer.is_valid():
                pages_serializer.save()
                page_id = pages_serializer.data["page"]
                for stakeholder in request.data['stakeholders']:
                    stakeholder['page'] = page_id
                    nested_serializer = Stakeholder_pageSerializer(data=stakeholder)
                    if  nested_serializer.is_valid():
                        nested_serializer.save()
                    # if the nested page is not valid it deletes the wrapper page created above
                    else:
                        page = pages.objects.get(page=page_id)
                        page.delete()
                        return Response(nested_serializer.data, status=status.HTTP_400_BAD_REQUEST)
                    #nested_serializer.save() #delete
                return Response(pages_serializer.data, status=status.HTTP_201_CREATED)

            # if the request was badly made or could not be created
            return Response(pages_serializer.data, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST) 

    # @api_view(['put'])
    def put(self, request):

        # takes the page_id from the url if the url has ?page_id=<id> at the end, no parameter passed return error 400
        page_id = self.request.query_params.get('page_id')

        # get all fields from this page_id if it doesn't exist return error 404
        try:
            page = pages.objects.get(page = page_id)
        except pages.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # please don't modify the scenario
        print(request.data)
        request.data["scenario_id"] = PagesSerializer(page).data['scenario']

        if request.method == "put": 
        
            page_type = request.data["page_type"]

            # check page.page_type = 'reflection'
            if (page_type == 'r'):
                pages_serializer = PagesSerializer(page, data=request.data)
                if pages_serializer.is_valid():
                    pages_serializer.save()
                    
                    # check that each reflectuon question already exists
                    for question in request.data['reflection_questions']:
                        try:
                            reflection_page = reflection_questions.objects.get(id = question.get('id'))
                        except:
                            # if the subpage does not exist, then you create that new page and post it and continue to the next component
                            question['page'] = page_id
                            nested_serializer = Reflection_questionsSerializer(data=question)
                            if nested_serializer.is_valid():
                                nested_serializer.save()
                            else:
                                return Response(nested_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                            continue

                        question['page'] = page_id
                        nested_serializer = Reflection_questionsSerializer(reflection_page, data=question)
                        if nested_serializer.is_valid():
                            nested_serializer.save()
                        else:
                            return Response(nested_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    return Response(pages_serializer.data, status=status.HTTP_200_OK)
                # else the request was badly made
                return Response(pages_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            # check page.page_type = 'action'
            if (page_type == 'a'):
                pages_serializer = PagesSerializer(page, data=request.data)
                if pages_serializer.is_valid():
                    pages_serializer.save()
                    
                    # check that each action_page already exists
                    for action in request.data['choices']:
                        try:
                            choices_page = action_page.objects.get(id = action.get('id'))
                        except:
                            # if the subpage does not exist, then you create that new page and post it and continue to the next component
                            action['page'] = page_id
                            nested_serializer = Action_pageSerializer(data=action)
                            if nested_serializer.is_valid():
                                nested_serializer.save()
                            else:
                                return Response(nested_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                            continue

                        action['page'] = page_id
                        nested_serializer = Action_pageSerializer(choices_page, data=action)
                        if nested_serializer.is_valid():
                            nested_serializer.save()
                        else:
                            return Response(nested_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    return Response(pages_serializer.data, status=status.HTTP_200_OK)
                # else the request was badly made
                return Response(pages_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            # check page.page_type = 'generic'
            if (page_type == 'g' or page_type == 'i'):
                pages_serializer = PagesSerializer(page, data=request.data)
                if pages_serializer.is_valid():
                    pages_serializer.save()
                    
                    # check that each generic page already exists
                    for body in request.data['bodies']:
                        try:
                            body_page = generic_page.objects.get(id = body.get('id'))
                        except:
                            # if the subpage does not exist, then you create that new page and post it and continue to the next component
                            body['page'] = page_id
                            nested_serializer = Generic_pageSerializer(data=body)
                            if nested_serializer.is_valid():
                                nested_serializer.save()
                            else:
                                return Response(nested_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                            continue

                        body['page'] = page_id
                        nested_serializer = Generic_pageSerializer(body_page, data=body)
                        if nested_serializer.is_valid():
                            nested_serializer.save()
                        else:
                            return Response(nested_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    return Response(pages_serializer.data, status=status.HTTP_200_OK)
                # else the request was badly made
                return Response(pages_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            # check page.page_type = 'stakeholders'
            if (page_type == 's'):
                pages_serializer = PagesSerializer(page, data=request.data)
                if pages_serializer.is_valid():
                    pages_serializer.save()
                    
                    # check that each stakeholder page already exists
                    for stakeholder in request.data['stakeholders']:
                        try:
                            page_stakeholder = stakeholder_to_page.objects.get(stakeholder = stakeholder.get('id'))
                        except:
                            # if the subpage does not exist, then you create that new page and post it and continue to the next component
                            stakeholder['page'] = page_id
                            nested_serializer = Stakeholder_pageSerializer(data=stakeholder)
                            if nested_serializer.is_valid():
                                nested_serializer.save()
                            else:
                                return Response(nested_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                            continue

                        stakeholder['page'] = page_id
                        nested_serializer = Stakeholder_pageSerializer(page_stakeholder, data=stakeholder)
                        if nested_serializer.is_valid():
                            nested_serializer.save()
                        else:
                            return Response(nested_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    return Response(pages_serializer.data, status=status.HTTP_200_OK)
                # else the request was badly made
                return Response(pages_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            # not a valid type of page
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST) 


    # @api_view(['delete'])
    def delete(self, request):

        # takes the page_id from the url if the url has ?page_id=<id> at the end, no parameter passed return error 400
        page_id = self.request.query_params.get('page_id')

        # check if the page exists.
        try: 
            page = pages.objects.get(page=page_id)
        except pages.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        
        # delete the page
        if (request.method == "delete"):

            #set next page field of pages pointing to the deleted page to be None/null
            next_pages = pages.objects.filter(next_page = page_id)
            for updated_page in next_pages:
                extant_page = updated_page
                updated_page.next_page = None
                updated_page_dict = PagesSerializer(updated_page).data
                pages_serializer = PagesSerializer(extant_page, data=updated_page_dict)
                if pages_serializer.is_valid():
                    pages_serializer.save()
                else:
                    print("error in making next_page = null during delete!")
                    return Response(pages_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            #also set and result_page fields pointing to the deleted page to be null as well.
            action_pages = action_page.objects.filter(result_page = page_id)
            for updated_page in action_pages:
                extant_page = updated_page
                updated_page.result_page = None
                updated_page_dict = Action_pageSerializer(updated_page).data
                action_pages_serializer = Action_pageSerializer(extant_page, data=updated_page_dict)
                if action_pages_serializer.is_valid():
                    action_pages_serializer.save()
                else:
                    print("error in making next_page = null during delete!")
                    return Response(action_pages_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            # finally delete the page 

            operation = page.delete()
            page_data = {}
            if (operation):
                page_data["success"] = "delete successful"
            else:
                page_data["failure"] = "delete failed"
            
            return Response(data=page_data)


# checked - ed - 4/15/2021
class student_info(APIView):
    def get(self,request,*args,**kwargs):
        scenario_id = self.request.query_params.get('scenario')
        responses_query = responses.objects.filter(scenario=scenario_id).values()
        student_ids = []
        data = []
        for response in responses_query:
            student = response['student']
            if student not in student_ids:
                date_taken = response['date_taken']
                student_ids.append(student)
        for student in student_ids:
            demographics_query = demographics.objects.filter(student = student).values()
            for dem in demographics_query:
                student_query = students.objects.filter(student = dem['student']).values()
                for x in student_query:
                    name = x['name']
            dem['name'] = name
            dem['date_taken'] = date_taken
            data.append(dem)
        return Response(data)


# seems like no change required - chirag - 4/15
class coverages_page(APIView):
    def get(self, request, *args, **kwargs):
        stakeholder_id = self.request.query_params.get('stakeholder_id')
        stkholder = {}
        # print(stakeholder_id)
        try: 
            coverage_list = coverage.objects.filter(stakeholder=stakeholder_id).values()
            # print("coverage list:", coverage_list)
        except coverage.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        issue_list = []
        # check for every single coverage object that belongs to the staheholder id 'id' 
        for coverages in coverage_list:
            issues_dict = {}
                # issuelist = coverageserializer(coverage.objects.get(issue=issueid)).data
                # issuelist.update({"name": issuesserializer(issues.objects.get(issue=issueid)).data['name']})
                # getting the issue for the coverage dictionary associated with the stakeholder_id
            try:
                issue = issues.objects.get(issue=coverages.get('issue_id'))
            except:
                continue
            issues_dict.update(coverages)
            # del issues_dict['id']
            # issues_dict['issue'] = issues_dict['issue_id']
            # del issues_dict['issue_id']
            # issues_dict['stakeholder'] = issues_dict['stakeholder_id']
            # del issues_dict['stakeholder_id']
            issues_dict.update(
                {
                    "name": issue.name
                })

            issue_list.append(issues_dict)
            
        stkholder.update(
            {
                "issues": issue_list
            }
        )

        return Response(stkholder, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        # """
        # docstring
        # """
        data = JSONParser().parse(request)

        if type(data) == list:
            response = []
            for item in data:
                stkholderid = item['stakeholder']
                issueid = item['issue']
                updatingitem = coverage.objects.get(
                    stakeholder=stkholderid, issue=issueid)
                serializer = coverageSerializer(
                    updatingitem, data=item)
                if serializer.is_valid():
                    serializer.save()
                    response.append(serializer.data)
                else:
                    return Response(response, status=status.HTTP_400_BAD_REQUEST)

            return Response(response, status=status.HTTP_200_OK)
        else:
            stkholderid = data['stakeholder']
            issueid = data['issue']
            updatingitem = coverage.objects.get(
                stakeholder=stkholderid, issue=issueid)
            serializer = coverageSerializer(
                updatingitem, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class stakeholders_page(APIView):
    
    def add_detail(self, stkholders):

        for stkholder in stkholders:
            stakeholder_id = stkholder['stakeholder']

            queryset = conversations.objects.filter(stakeholder=stakeholder_id)
            conlist = ConversationsSerializer(queryset, many=true).data
            stkholder['conversations'] = conlist

            try: 
                coverage_list = coverage.objects.filter(stakeholder=stakeholder_id).values()
            except coverage.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            issue_list = []
            # check for every single coverage object that belongs to the staheholder id 'id' 
            for coverages in coverage_list:
                issues_dict = {}
                # issuelist = coverageserializer(coverage.objects.get(issue=issueid)).data
                # issuelist.update({"name": issuesserializer(issues.objects.get(issue=issueid)).data['name']})
                # getting the issue for the coverage dictionary associated with the stakeholder_id
                try:
                    issue = issues.objects.get(issue=coverages.get('issue'))
                except:
                    continue
                issues_dict.update(coverages)
                # del issues_dict['id']
                # issues_dict['issue'] = issues_dict['issue_id']
                # del issues_dict['issue_id']
                # issues_dict['stakeholder'] = issues_dict['stakeholder_id']
                # del issues_dict['stakeholder_id']
                issues_dict.update(
                    {
                        "name": issue.name
                    })

                issue_list.append(issues_dict)
            
            stkholder.update(
                {
                    "issues": issue_list
                }
            )

        return stkholders

#         '''
#         page_data = pagesserializer(page).datapage_data.update(
#                 {
#                     "reflection_questions": reflection_query
#                 }
#             )
#  reflection_query = reflection_questions.objects.filter(page = page_id).values()
#             page_data.update(
#                 {
#                     "reflection_questions": reflection_query
#                 }
#             )
#         '''

    def get(self, request, *args, **kwargs):
        '''
        return format
        [
            {
                "stakeholder": 3,
                "name": "mon",
                "description": "this is mon",
                "job": "driver",
                "introduction": "mon is a driver",
                "scenario": 1,
                "version": 1,
                "conversations": [
                    {
                        "conversation": 4,
                        "question": "question 1",
                        "response": "answer 1",
                        "stakeholder": 3
                    }
                ],
                "issues": [
                    {
                        "issue": 4,
                        "name": "issue 3",
                        "importance_score": 10.0,
                        "scenario": 1,
                        "version": 1
                    }
                ]
            },
        ]
        parse scenario_id and stakeholder_id from the request url
        example
        http://127.0.0.1:8000/stakeholders?scenario_id=3
        http://127.0.0.1:8000/stakeholders?stakeholder_id=0
        '''
        # scenario not id
        scenario_id = self.request.query_params.get('scenario_id')
        stakeholder_id = self.request.query_params.get('stakeholder_id')
        # stakeholder_id = self.request.get.get('stakeholder_id')

        # handle request for scenario_id
        # get all stakeholder in scenario with id = scenario_id
        if scenario_id != None:
            # checking valid scenario id
            try:
                # return empty if scenario doesn't have any stakeholder
                # return list of stakeholder belong to that scenario
                scenarios.objects.get(scenario_id = scenario_id)
                queryset = stakeholders.objects.filter(
                    scenario=scenario_id)
                data = list(StakeholdersSerializer(queryset, many=true).data)
                data = self.add_detail(data)
                return Response(data, status=status.HTTP_200_OK)

            # return an error for non-existed scenario id
            except scenarios.DoesNotExist:
                message = {'message': 'invalid scenario id'}
                return Response(message, status=status.HTTP_404_NOT_FOUND)

        # handle request for stakeholder_id
        # get the stakeholder id = stakeholder_id
        if stakeholder_id != None:
            try:
                queryset = stakeholders.objects.filter(
                    stakeholder=stakeholder_id)
                data = list(StakeholdersSerializer(queryset, many=true).data)
                data = self.add_detail(data)
                return Response(data, status=status.HTTP_200_OK)

            except stakeholders.DoesNotExist:
                message = {'message': 'invalid stakeholder id'}
                return Response(message, status=status.HTTP_404_NOT_FOUND)

        queryset = stakeholders.objects.all()
        data = StakeholdersSerializer(queryset, many=true).data
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
    
        serializer = StakeholdersSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            stkholderid = serializer.data['stakeholder']
            scenarioid = serializer.data['scenario']
            stkholderversion = serializer.data['version']
            queryset = issues.objects.filter(scenario_id=scenarioid)
            data = issuesserializer(queryset, many=true).data
            for item in data:
                itemdict = {}
                itemdict['stakeholder'] = stkholderid
                itemdict['stakeholder_version'] = stkholderversion
                itemdict['issue'] = item['issue']
                itemdict['name'] = item['name']
                itemdict['coverage_score'] = 0
                print(itemdict)
                itemserializer = coverageSerializer(data=itemdict)
                if itemserializer.is_valid():
                    itemserializer.save()
                else:
                    return Response(itemSerializer.errors,
                                    status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):

        stakeholder_id = self.request.query_params.get('stakeholder_id')

        if stakeholder_id != None:
            try:
                response = stakeholders.objects.get(
                    stakeholder =stakeholder_id)
                response.delete()
                return Response({'message': 'deleted'}, status=status.HTTP_202_ACCEPTED)
            except stakeholders.doesnotexist:
                return Response({'message': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'message': 'missing id'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        '''
        put can take one object or a list
        for one object put
        {
            "stakeholder": 1,
            "name": "stakeholder 1a",
            "description": "description 1",
            "job": "job 1",
            "introduction": "introduction 1",
            "scenario": 1,
            "version": 1
        }
        for list put
        [
            {
                "stakeholder": 1,
                "name": "stakeholder 1a",
                "description": "description 1",
                "job": "job 1",
                "introduction": "introduction 1",
                "scenario": 1,
                "version": 1
            },
            {
                "stakeholder": 2,
                "name": "stakeholder 2a",
                "description": "description 2",
                "job": "job 2",
                "introduction": "introduction 2",
                "scenario": 1,
                "version": 1
            }
        ]
        '''
        data = JSONParser().parse(request)

        if type(data) == list:
            response = []
            for item in data:
                id = item['stakeholder']
                updatingitem = stakeholders.objects.get(stakeholder=id)
                stkholderserializer = StakeholdersSerializer(
                    updatingitem, data=item)
                if stkholderserializer.is_valid():
                    stkholderserializer.save()
                    response.append(stkholderserializer.data)
                else:
                    return Response(response, status=status.HTTP_400_BAD_REQUEST)

            return Response(response, status=status.HTTP_200_OK)
        else:
            id = data['stakeholder']
            updatingitem = stakeholders.objects.get(stakeholder=id)
            stkholderserializer = StakeholdersSerializer(
                updatingitem, data=data)
            if stkholderserializer.is_valid():
                stkholderserializer.save()
                return Response(stkholderserializer.data, status=status.HTTP_200_OK)
            else:
                return Response(stkholderserializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class coverages_page(APIView):


# checked - ed - 4/15/2021
class student_responses(APIView):
    def get(self, request, *args, **kwargs):

        #filter by scenario and student id 
        scenario = self.request.query_params.get('scenario')
        student = self.request.query_params.get('student')
        filterargs = {'scenario':scenario,'student':student}
        responses_query = responses.objects.filter(**filterargs).values()
        choice_array = []
        choices_array = []
        choices_dict = {}
        #get the different actions
        for response in responses_query:
            #filter by page number 
            name_query = pages.objects.filter(page = response["action_page"]).values()

            for name in name_query:
                name = name['page_title']
                type = name['page_type']
            choices_query = action_page.objects.filter(page = response["action_page"]).values()
            for choice in choices_query:
                choice_array.append(choice['choice'])
            chosen_query = responses.objects.filter(action_page = response["action_page"]).values()
            for chose in chosen_query:
                chosen = chose['choice']
                date_taken = chose['date_taken']
            #only if it is an action page
            choices_dict = {"name": name, "choices":choice_array, "chosen": chosen, "date_taken": date_taken }
            choices_array.append(choices_dict)
            choice_array = []
        reflections_array = []
        reflections_dict = {}
        #get the different reflections
        reflections_query = reflections_taken.objects.filter(**filterargs).values()
        for reflection in reflections_query:
            name_query = pages.objects.filter(page = reflection["page"]).values()
            for name in name_query:
                name = name['page_title']
                type = name['page_type']
            ref_questions_query = reflection_question_to_page.objects.filter(page_id = reflection["page"]).values()
            for question in ref_questions_query:
                question = question['reflection_question']
                date_taken = answer['date_taken']
            ref_answers_query = reflections_taken.objects.filter(response_id = reflection["response_id"]).values()
            for answer in ref_answers_query:
                reflection = answer['reflections']
                # 
                #only if it is a reflection page 
            reflections_dict = {"name": name, "question": question, "reflection": reflection, "date_taken": date_taken}
            reflections_array.append(reflections_dict)
        data_dict = {}
        data_dict["choices"] = choices_array
        data_dict["reflections"] = reflections_array
        return Response(data_dict)