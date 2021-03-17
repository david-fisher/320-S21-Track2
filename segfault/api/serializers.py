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


# response, reflections taken, response_to_action_page, conversations had, student times

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