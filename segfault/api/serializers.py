from rest_framework import serializers
from api.models import *

#TODO: Need to disable for all non-admin after depolying(security)
class ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenario
        fields = ['id','name','date_created','course']
    
    
#TODO: Need to disable for all non-admin after depolying(security)
class StudentSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Student
        fields = ['first_name','last_name']
    
class CourseSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Course
        fields = ['name','students','id']


class ConversationSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Conversation
        fields = '__all__'

class DemographicSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Demographic
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
        model = pages
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

#page types serializer
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