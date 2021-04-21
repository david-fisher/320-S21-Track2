from rest_framework import serializers
from .models import *
# demographics, students, professors, scenarios, stakeholder_page, stakeholders, conversations


class DemographicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DEMOGRAPHICS
        fields = ('STUDENT', 'AGE', 'GRADE', 'GENDER', 'RACE', 'MAJOR')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = STUDENTS
        fields = ('STUDENT', 'FNAME', 'LNAME')

class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = QUESTIONS
        fields = ('QUESTION', 'VERSION', 'POINTS', 'QUESTION_TEXT', 'QUESTION_SUMMARY')

class StudentTimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = STUDENT_TIMES
        fields = ('STUDENT', 'SCENARIO_ID', 'COURSE',
                  'DATE_TAKEN', 'PAGE', 'END_TIME', 'START_TIME')


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PROFESSORS
        fields = ('PROFESSOR', 'FNAME', 'LNAME')


class ScenariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = SCENARIOS
        fields = ('SCENARIO', 'VERSION', 'NAME', 'IS_FINISHED',
                  'PUBLIC', 'NUM_CONVERSATION', 'DATE_CREATED', 'SCENARIO_ID')


class PagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PAGES
        fields = ('PAGE', 'PAGE_TYPE', 'PAGE_TITLE', 'BODY', 'SCENARIO',
                  'VERSION', 'NEXT_PAGE', 'X_COORDINATE', 'Y_COORDINATE', 'NEXT_PAGE_VERSION')


class Stakeholder_to_pageSerializer(serializers.ModelSerializer):
    class Meta:
        model = STAKEHOLDER_TO_PAGE
        fields = ('PAGE', 'PAGE_VERSION', 'STAKEHOLDER', 'STAKEHOLDER_VERSION')


class Reflection_questionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = REFLECTION_QUESTIONS
        fields = ('REFLECTION_QUESTION', 'ID', 'VERSION')

class Reflection_questions_to_pageSerializer(serializers.ModelSerializer):
    class Meta:
        model = REFLECTION_QUESTION_TO_PAGE
        fields = '__all__'


class StakeholdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = STAKEHOLDERS
        fields = '__all__'


class ConversationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CONVERSATIONS
        fields = ('STAKEHOLDER', 'STAKEHOLDER_VERSION', 'CONVERSATION', 'QUESTION', 'RESPONSE')

class Courses_to_ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = COURSES_TO_SCENARIO
        fields = '__all__'

class ReflectionsTakenSerializer(serializers.ModelSerializer):
    class Meta:
        model = REFLECTIONS_TAKEN
        fields = ('REFLECTIONS', 'RESPONSE_ID')


# class ConversationsHadSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = conversations_had
#         fields = '__all__'


class StudentsToCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = STUDENTS_TO_COURSE
        fields = ('STUDENT', 'COURSE')


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = COURSES
        fields = ('COURSE', 'NAME')


class ResponsesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RESPONSES
        fields = ('RESPONSE'), ('STUDENT'), ('SCENARIO'), ('PAGE'), (
            'COURSE'), ('DATE_TAKEN'), ('CHOICE'), ('VERSION'), ('RESPONSE_ID')


class PagesToScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PAGES_TO_SCENARIO
        fields = ('PAGE_ID'), ('SCENARIO_ID'), ('PAGE_VERSION'), ('SCENARIO_VERSION')


class allScenariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = SCENARIOS
        fields = ('SCENARIO', 'NAME', 'IS_FINISHED', 'PROFESSOR')


class Scenarios_forSerializer(serializers.ModelSerializer):
    class Meta:
        model = SCENARIOS_FOR
        fields = ('SCENARIO_ID', 'COURSE')


class Generic_pageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GENERIC_PAGE
        fields = ('PAGE', 'BODY', 'ID', 'VERSION')


class Professors_to_coursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PROFESSORS_TO_COURSES
        fields = ('PROFESSOR', 'COURSE')


class Professors_to_scenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PROFESSORS_TO_SCENARIO
        fields = ('PROFESSOR', 'COURSE', 'PERMISSION')

class Responses_to_ConversationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RESPONSES_TO_CONVERSATIONS
        fields = ('RESPONSE_ID', 'STAKEHOLDER', 'SCORE', 'CONVERSATION' )

class IssuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ISSUES
        fields = '__all__'


class Action_pageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ACTION_PAGE
        fields = '__all__'

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


class coverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = COVERAGE
        fields = ('STAKEHOLDER', 'STAKEHOLDER_VERSION','ISSUE', 'COVERAGE_SCORE')


# class Actions_takenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = actions_taken
#         fields = '__all__'
