from rest_framework import serializers
from .models import *
# demographics, students, professors, scenarios, stakeholder_page, stakeholders, conversations

#need     1.) stakeholders_to_questions

#updated 05/04/21
class StakeholdersToQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = stakeholders_to_questions
        fields = ('stakeholder', 'question', 'id')

#updated 05/04/21
class DemographicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = demographics
        fields = ('student', 'age', 'grade', 'gender', 'race', 'major')

#updated 05/04/21
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = students
        fields = ('student', 'fname', 'lname')

#updated 05/04/21
class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = questions
        fields = ('question', 'version', 'points', 'question_text', 'question_summary', 'id')

#updated 05/04/21
class StudentTimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = student_times
        fields = ('student', 'scenario_id', 'course',
                  'date_taken', 'page', 'end_time', 'start_time', 'id')

#updated 05/04/21
class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = professors
        fields = ('professors', 'fname', 'lname')

#updated 05/04/21
class ScenariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = scenarios
        fields = ('scenario', 'version', 'name', 'is_finished',
                  'public', 'num_conversation', 'date_created', 'scenario_id')

#updated 05/04/21
class PagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = pages
        fields = ('page', 'page_type', 'page_title', 'body', 'scenario',
                  'version', 'next_id', 'x_coordinate', 'y_coordinate', 'complete', 'id')

#updated 05/04/21
class Stakeholder_to_pageSerializer(serializers.ModelSerializer):
    class Meta:
        model = stakeholders_to_page
        fields = ('page', 'stakeholder', 'id')

#updated 05/04/21
class Reflection_questionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = reflection_questions
        fields = ('reflection_question', 'reflection_question_id', 'id', 'version')

#updated 05/04/21 -- didnt do anything fields = all
class Reflection_questions_to_pageSerializer(serializers.ModelSerializer):
    class Meta:
        model = reflection_questions_to_page
        fields = '__all__'

#updated 05/04/21 --- didnt do anything since fileds = all
class StakeholdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = stakeholders
        fields = '__all__'

#updated 05/04/21
class ConversationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = conversations
        fields = ('stakeholder', 'points', 'conversation', 'question', 'question_summary', 'response')

#updated 05/04/21 -- didnt do anything fields = all
class Courses_to_ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = courses_to_scenario
        fields = '__all__'

#updated 05/04/21
class ReflectionsTakenSerializer(serializers.ModelSerializer):
    class Meta:
        model = reflections_taken
        fields = ('reflections', 'response_id')


# class ConversationsHadSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = conversations_had
#         fields = '__all__'

#updated 05/04/21
class StudentsToCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = students_to_course
        fields = ('student', 'course', 'id')

#updated 05/04/21
class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = courses
        fields = ('course', 'name')

#updated 05/04/21
class ResponsesSerializer(serializers.ModelSerializer):
    class Meta:
        model = responses
        fields = ('response', 'student', 'scenario', 'page', 
            'course', 'date_taken', 'choice', 'version', 'response_id')

#updated 05/04/21
class PagesToScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = pages_to_scenario
        fields = ('page_id', 'scenario_id', 'id')


#class allScenariosSerializer(serializers.ModelSerializer):
    #class Meta:
       # model = SCENARIOS
        #fields = ('SCENARIO', 'NAME', 'IS_FINISHED', 'PROFESSOR')

#updated 05/04/21
class Scenarios_forSerializer(serializers.ModelSerializer):
    class Meta:
        model = scenarios_for
        fields = ('scenario_id', 'course', 'version', 'id')

#updated 05/04/21
class Generic_pageSerializer(serializers.ModelSerializer):
    class Meta:
        model = generic_page
        fields = ('generic_page_id', 'page', 'body', 'id', 'version')

#updated 05/04/21
class Professors_to_coursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = professors_to_courses
        fields = ('professor', 'course', 'id')

#updated 05/04/21
class Professors_to_scenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = professors_to_scenario
        fields = ('professor', 'scenario', 'permission', 'id')

#updated 05/04/21
class Responses_to_ConversationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = responses_to_conversations
        fields = ('response_id', 'stakeholder', 'stakeholder_version', 'score', 'conversation', 'id')

#updated 05/04/21 -- didnt do anything since fields= all
class IssuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = issues
        fields = '__all__'

#updated 05/04/21 -- didnt do anything fields=all
class Action_pageSerializer(serializers.ModelSerializer):
    class Meta:
        model = action_page
        fields = '__all__'

#updated 05/04/21 -- didnt do anything fields = all
class Response_to_action_pageSerializer(serializers.ModelSerializer):
    class Meta:
        model = response_to_action_page
        fields = '__all__'

# Serializers for page types
#class Pages_reflectionSerializer(serializers.ModelSerializer):
    #reflection_question = Reflection_questionsSerializer()
    #class Meta:
       # model = PAGES
        #fields = '__all__'


#class Pages_actionSerializer(serializers.ModelSerializer):
    #action_page = Action_pageSerializer()

    #class Meta:
       # model = PAGES
       # fields = '__all__'


#class Pages_genericSerializer(serializers.ModelSerializer):
    #generic_page = Generic_pageSerializer()

    #class Meta:
       # model = PAGES
        #fields = '__all__'


#class Pages_stakeholderSerializer(serializers.ModelSerializer):
    #stakeholder_page = Stakeholder_to_pageSerializer()

    #class Meta:
       # model = PAGES
        #fields = '__all__'

#updated 05/04/21
class coverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = coverage
        fields = ('stakeholder', 'id', 'issue', 'coverage_score')


# class Actions_takenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = actions_taken
#         fields = '__all__'
