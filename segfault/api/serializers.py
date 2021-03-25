from rest_framework import serializers
from api.models import *


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('course', 'name', 'students', 'professors','scenarios')

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


class Stakeholder_pageSerializer(serializers.ModelSerializer):
    class Meta:
        model = stakeholder_page
        fields = '__all__'


class Reflection_questionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = reflection_questions
        fields = '__all__'


class Action_pageSerializer(serializers.ModelSerializer):
    class Meta:
        model = action_page
        fields = '__all__'


class Generic_pageSerializer(serializers.ModelSerializer):
    class Meta:
        model = generic_page
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
    stakeholder_page = Stakeholder_pageSerializer()

    class Meta:
        model = Pages


class ReflectionsTakenSerializer(serializers.ModelSerializer):
    class Meta:
        model = reflections_taken
        fields = '__all__'


class ResponseToActionPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = response_to_action_page
        fields = '__all__'


class ConversationsHadSerializer(serializers.ModelSerializer):
    class Meta:
        model = conversations_had
        fields = '__all__'


class StudentTimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = student_times
        fields = '__all__'


class CoverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coverage
        fields = '__all__'


class StakeholderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stakeholders
        fields = '__all__'

