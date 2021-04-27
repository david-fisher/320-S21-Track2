from rest_framework import serializers
from api.models import *


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'

# TODO: Need to disable for all non-admin after depolying(security)


class StudentSerializer(serializers.ModelSerializer):
    enrolled_class = serializers.PrimaryKeyRelatedField(
        many=True, source='courses', read_only=True)

    class Meta:
        model = Students
        fields = '__all__'


class ProfessorSerializer(serializers.ModelSerializer):
    teaching_class = serializers.PrimaryKeyRelatedField(
        many=True, source='courses', read_only=True)

    class Meta:
        model = Professors
        fields = '__all__'


class DemographicSerializer(serializers.ModelSerializer):
    student_info = StudentSerializer(source='student',read_only=True)

    class Meta:
        model = Demographics
        fields = '__all__'
        depth = 3


class ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenarios
        fields = '__all__'


class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversations
        fields = '__all__'


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responses
        fields = '__all__'


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issues
        fields = '__all__'


class PagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pages
        fields = '__all__'


class Stakeholder_to_pageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StakeholderToPage
        fields = '__all__'


class Reflection_questionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReflectionQuestions
        fields = '__all__'


class Action_pageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionPage
        fields = '__all__'


class Generic_pageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenericPage
        fields = '__all__'

# page types serializer


class Pages_reflectionSerializer(serializers.ModelSerializer):
    reflection_question = Reflection_questionsSerializer()

    class Meta:
        model = Pages
        fields = '__all__'


class Pages_actionSerializer(serializers.ModelSerializer):
    action_page = Action_pageSerializer()

    class Meta:
        model = Pages
        fields = '__all__'


class Pages_genericSerializer(serializers.ModelSerializer):
    generic_page = Generic_pageSerializer()

    class Meta:
        model = Pages
        fields = '__all__'


class Pages_stakeholderSerializer(serializers.ModelSerializer):
    stakeholder_page = Stakeholder_to_pageSerializer()

    class Meta:
        model = Pages


class ReflectionsTakenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReflectionsTaken
        fields = '__all__'


class ResponseToActionPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponseToActionPage
        fields = '__all__'


class Responses_to_conversationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponsesToConversations
        fields = '__all__'


class StudentTimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentTimes
        fields = '__all__'


class CoverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coverage
        fields = '__all__'


class StakeholderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stakeholders
        fields = '__all__'

# class Student_page_progressSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student_page_progress
#         fields = '__all__'

class StudentToCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentsToCourse
        fields = '__all__'

class ScenarioForSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScenariosFor
        fields = '__all__'

class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'

class StakeholdersToQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StakeholdersToQuestions
        fields = '__all__'

class PagesToScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PagesToScenario
        fields = '__all__'

class ReflectionQuestionToPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReflectionQuestionToPage
        fields = '__all__'

class ProfessorsToScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessorsToScenario
        fields = '__all__'

class ProfessorsToCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessorsToCourses
        fields = '__all__'
