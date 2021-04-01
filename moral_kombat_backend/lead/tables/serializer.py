from rest_framework import serializers
from .models import *
# demographics, students, professors, scenarios, stakeholder_page, stakeholders, conversations


class DemographicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = demographics
        fields = ('STUDENT', 'AGE', 'GRADE', 'GENDER', 'RACE', 'MAJOR')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = students
        fields = ('STUDENT', 'FNAME', 'LNAME')


class StudentTimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = student_times
        fields = ('STUDENT', 'SCENARIO_ID', 'COURSE',
                  'DATE_TAKEN', 'PAGE', 'END_TIME', 'START_TIME')


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = professors
        fields = ('PROFESSOR', 'FNAME', 'LNAME')


class ScenariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = scenarios
        fields = ('SCENARIO', 'VERSION', 'NAME', 'IS_FINISHED',
                  'PUBLIC', 'NUM_CONVERSATION', 'PROFESSOR', 'SCENARIO_ID')


class PagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = pages
        fields = ('PAGE', 'PAGE_TYPE', 'PAGE_TITLE', 'BODY', 'SCENARIO',
                  'VERSION', 'NEXT_PAGE', 'X_COORDINATE', 'Y_COORDINATE')


class Stakeholder_to_pageSerializer(serializers.ModelSerializer):
    class Meta:
        model = stakeholder_to_page
        fields = ('PAGE', 'STAKEHOLDER')


class Reflection_questionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = reflection_questions
        fields = ('PAGE', 'REFLECTION_QUESTION', 'id', 'VERSION')

class Reflection_questions_to_pageSerializer(serializers.ModelSerializer):
    class Meta:
        model = reflection_question_to_page
        fields = '__all__'


class StakeholdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = stakeholders
        fields = '__all__'


class ConversationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = conversations
        fields = ('STAKEHOLDER', 'CONVERSATION', 'QUESTION', 'RESPONSE')

class Courses_to_ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = courses_to_scenario
        fields = '__all__'

class ReflectionsTakenSerializer(serializers.ModelSerializer):
    class Meta:
        model = reflections_taken
        fields = ('REFLECTIONS', 'RESPONSE_ID')


# class ConversationsHadSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = conversations_had
#         fields = '__all__'


class StudentsToCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = students_to_course
        fields = ('STUDENT', 'COURSE')


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = courses
        fields = ('COURSE', 'NAME')


class ResponsesSerializer(serializers.ModelSerializer):
    class Meta:
        model = responses
        fields = ('RESPONSE'), ('STUDENT'), ('SCENARIO'), ('PAGE'), (
            'COURSE'), ('DATE_TAKEN'), ('CHOICE'), ('VERSION'), ('RESPONSE_ID')


class PagesToScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = pages_to_scenario
        fields = (
            'page_id'), ('scenario_id'), ('page_version'), ('scenario_version')


class allScenariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = scenarios
        fields = ('SCENARIO', 'NAME', 'IS_FINISHED', 'PROFESSOR')


class Scenarios_forSerializer(serializers.ModelSerializer):
    class Meta:
        model = scenarios_for
        fields = ('SCENARIO_ID', 'COURSE')


class Generic_pageSerializer(serializers.ModelSerializer):
    class Meta:
        model = generic_page
        fields = ('PAGE', 'BODY')


class Professors_to_coursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = professors_to_courses
        fields = ('PROFESSOR', 'COURSE')


class Professors_to_scenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = professors_to_scenario
        fields = ('PROFESSOR', 'COURSE', 'PERMISSION')

class Responses_to_ConversationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = responses_to_conversations
        fields = ('RESPONSE_ID', 'STAKEHOLDER', 'SCORE', 'CONVERSATION' )

class IssuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issues
        fields = '__all__'


class Action_pageSerializer(serializers.ModelSerializer):
    class Meta:
        model = action_page
        fields = '__all__'

class Response_to_action_pageSerializer(serializers.ModelSerializer):
    class Meta:
        model = response_to_action_page
        fields = '__all__'

# Serializers for page types
class Pages_reflectionSerializer(serializers.ModelSerializer):
    reflection_question = Reflection_questionsSerializer()

    class Meta:
        model = pages
        fields = '__all__'


class Pages_actionSerializer(serializers.ModelSerializer):
    action_page = Action_pageSerializer()

    class Meta:
        model = pages
        fields = '__all__'


class Pages_genericSerializer(serializers.ModelSerializer):
    generic_page = Generic_pageSerializer()

    class Meta:
        model = pages
        fields = '__all__'


class Pages_stakeholderSerializer(serializers.ModelSerializer):
    stakeholder_page = Stakeholder_pageSerializer()

    class Meta:
        model = pages
        fields = '__all__'


class coverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = coverage
        fields = ('STAKEHOLDER', 'ISSUE', 'COVERAGE_SCORE')


# class Actions_takenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = actions_taken
#         fields = '__all__'
