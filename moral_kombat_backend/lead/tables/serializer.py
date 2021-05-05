from rest_framework import serializers
from .models import *
# demographics, students, professors, scenarios, stakeholder_page, stakeholders, conversations

#need     1.) stakeholders_to_questions

#updated 05/04/21
class StakeholdersToQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = STAKEHOLDERS_TO_QUESTIONS
        fields = ('STAKEHOLDER', 'QUESTION', 'ID')

#updated 05/04/21
class DemographicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DEMOGRAPHICS
        fields = ('STUDENT', 'AGE', 'GRADE', 'GENDER', 'RACE', 'MAJOR')

#updated 05/04/21
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = STUDENTS
        fields = ('STUDENT', 'FNAME', 'LNAME')

#updated 05/04/21
class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = QUESTIONS
        fields = ('QUESTION', 'VERSION', 'POINTS', 'QUESTION_TEXT', 'QUESTION_SUMMARY', 'ID')

#updated 05/04/21
class StudentTimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = STUDENT_TIMES
        fields = ('STUDENT', 'SCENARIO_ID', 'COURSE',
                  'DATE_TAKEN', 'PAGE', 'END_TIME', 'START_TIME', 'ID')

#updated 05/04/21
class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PROFESSORS
        fields = ('PROFESSOR', 'FNAME', 'LNAME')

#updated 05/04/21
class ScenariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = SCENARIOS
        fields = ('SCENARIO', 'VERSION', 'NAME', 'IS_FINISHED',
                  'PUBLIC', 'NUM_CONVERSATION', 'DATE_CREATED', 'SCENARIO_ID')

#updated 05/04/21
class PagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PAGES
        fields = ('PAGE', 'PAGE_TYPE', 'PAGE_TITLE', 'BODY', 'SCENARIO',
                  'VERSION', 'NEXT_ID', 'X_COORDINATE', 'Y_COORDINATE', 'COMPLETED', 'ID')

#updated 05/04/21
class Stakeholder_to_pageSerializer(serializers.ModelSerializer):
    class Meta:
        model = STAKEHOLDER_TO_PAGE
        fields = ('PAGE', 'STAKEHOLDER', 'ID')

#updated 05/04/21
class Reflection_questionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = REFLECTION_QUESTIONS
        fields = ('REFLECTION_QUESTION', 'REFLECTION_QUESTION_ID', 'ID', 'VERSION')

#updated 05/04/21 -- didnt do anything fields = all
class Reflection_questions_to_pageSerializer(serializers.ModelSerializer):
    class Meta:
        model = REFLECTION_QUESTION_TO_PAGE
        fields = '__all__'

#updated 05/04/21 --- didnt do anything since fileds = all
class StakeholdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = STAKEHOLDERS
        fields = '__all__'

#updated 05/04/21
class ConversationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CONVERSATIONS
        fields = ('STAKEHOLDER', 'POINTS', 'CONVERSATION', 'QUESTION', 'QUESTION_SUMMARY', 'RESPONSE')

#updated 05/04/21 -- didnt do anything fields = all
class Courses_to_ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = COURSES_TO_SCENARIO
        fields = '__all__'

#updated 05/04/21
class ReflectionsTakenSerializer(serializers.ModelSerializer):
    class Meta:
        model = REFLECTIONS_TAKEN
        fields = ('REFLECTIONS', 'RESPONSE_ID')


# class ConversationsHadSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = conversations_had
#         fields = '__all__'

#updated 05/04/21
class StudentsToCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = STUDENTS_TO_COURSE
        fields = ('STUDENT', 'COURSE', 'ID')

#updated 05/04/21
class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = COURSES
        fields = ('COURSE', 'NAME')

#updated 05/04/21
class ResponsesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RESPONSES
        fields = ('RESPONSE', 'STUDENT', 'SCENARIO', 'PAGE', 
            'COURSE', 'DATE_TAKEN', 'CHOICE', 'VERSION', 'RESPONSE_ID')

#updated 05/04/21
class PagesToScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PAGES_TO_SCENARIO
        fields = ('PAGE_ID', 'SCENARIO_ID', 'ID')


class allScenariosSerializer(serializers.ModelSerializer):
    class Meta:
       model = SCENARIOS
       fields = ('SCENARIO', 'NAME', 'IS_FINISHED', 'PROFESSOR')

#updated 05/04/21
class Scenarios_forSerializer(serializers.ModelSerializer):
    class Meta:
        model = SCENARIOS_FOR
        fields = ('SCENARIO_ID', 'COURSE', 'VERSION', 'ID')

#updated 05/04/21
class Generic_pageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GENERIC_PAGE
        fields = ('GENERIC_PAGE_ID', 'PAGE', 'BODY', 'ID', 'VERSION')

#updated 05/04/21
class Professors_to_coursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PROFESSORS_TO_COURSES
        fields = ('PROFESSOR', 'COURSE', 'ID')

#updated 05/04/21
class Professors_to_scenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PROFESSORS_TO_SCENARIO
        fields = ('PROFESSOR', 'SCENARIO', 'PERMISSION', 'ID')

#updated 05/04/21
class Responses_to_ConversationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RESPONSES_TO_CONVERSATIONS
        fields = ('RESPONSE_ID', 'STAKEHOLDER', 'STAKEHOLDER_VERSION', 'SCORE', 'CONVERSATION', 'ID')

#updated 05/04/21 -- didnt do anything since fields= all
class IssuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ISSUES
        fields = '__all__'

#updated 05/04/21 -- didnt do anything fields=all
class Action_pageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ACTION_PAGE
        fields = '__all__'

#updated 05/04/21 -- didnt do anything fields = all
class Response_to_action_pageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RESPONSE_TO_ACTION_PAGE
        fields = '__all__'

# Serializers for page types
class Pages_reflectionSerializer(serializers.ModelSerializer):
    reflection_question = Reflection_questionsSerializer()
    class Meta:
       model = PAGES
       fields = '__all__'


class Pages_actionSerializer(serializers.ModelSerializer):
    action_page = Action_pageSerializer()

    class Meta:
       model = PAGES
       fields = '__all__'


class Pages_genericSerializer(serializers.ModelSerializer):
    generic_page = Generic_pageSerializer()

    class Meta:
       model = PAGES
       fields = '__all__'


class Pages_stakeholderSerializer(serializers.ModelSerializer):
    stakeholder_page = Stakeholder_to_pageSerializer()

    class Meta:
       model = PAGES
       fields = '__all__'

#updated 05/04/21
class coverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = COVERAGE
        fields = ('STAKEHOLDER', 'ID', 'ISSUE', 'COVERAGE_SCORE')


# class Actions_takenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = actions_taken
#         fields = '__all__'
