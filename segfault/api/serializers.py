from rest_framework import serializers
from api.models import *

#TODO: Need to disable for all non-admin after depolying(security)
class ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenario
        fields = ['id','name','date_created','course']
    
    
#TODO: Need to disable for all non-admin after depolying(security)
class UserSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Webuser
        fields = ['url','id','username']
    
class CourseSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Course
        fields = ['name','fullName','semester','students','scenarios','id']

class PartOfSerializer(serializers.ModelSerializer):
    course_name = serializers.ReadOnlyField(source= 'course.name')
    scenario_name =  serializers.ReadOnlyField(source= 'scenario.name')
    
    class Meta:
        model = PartOf
        fields = ['scenario','course','course_name','scenario_name']


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
