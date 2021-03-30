from rest_framework import serializers
from api.models import *


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

# TODO: Need to disable for all non-admin after depolying(security)


class StudentSerializer(serializers.ModelSerializer):
    enrolled_class = serializers.PrimaryKeyRelatedField(
        many=True, source='courses', read_only=True)

    class Meta:
        model = Student
        fields = '__all__'


class ProfessorSerializer(serializers.ModelSerializer):
    teaching_class = serializers.PrimaryKeyRelatedField(
        many=True, source='courses', read_only=True)

    class Meta:
        model = Professor
        fields = '__all__'


class DemographicSerializer(serializers.ModelSerializer):
    student_info = StudentSerializer(source='student',read_only=True)

    class Meta:
        model = Demographic
        fields = '__all__'
        depth = 3


class ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenario
        fields = '__all__'


class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversations
        fields = '__all__'


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = '__all__'


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'


class PagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pages
        fields = '__all__'


class Stakeholder_to_pageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stakeholder_to_page
        fields = '__all__'


class Reflection_questionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reflection_questions
        fields = '__all__'


class Action_pageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action_page
        fields = '__all__'


class Generic_pageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Generic_page
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
        model = Reflections_taken
        fields = '__all__'


class ResponseToActionPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response_to_action_page
        fields = '__all__'


class Responses_to_conversationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responses_to_conversations
        fields = '__all__'


class StudentTimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_times
        fields = '__all__'


class CoverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coverage
        fields = '__all__'


class StakeholderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stakeholders
        fields = '__all__'

class Student_page_progressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_page_progress
        fields = '__all__'

class StudentToCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_to_Course
        fields = '__all__'

class ScenarioToCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenario_to_Course
        fields = '__all__'