from rest_framework import serializers
from api.models import *

#TODO: Need to disable for all non-admin after depolying(security)
class ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenarios
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
        model = Conversations
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
        model = Issues
        fields = '__all__'

class CoverageSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Coverage
        fields = '__all__'

class StakeholderSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Stakeholders
        fields = '__all__'

class ScenariosForSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Scenarios_for
        fields = '__all__'

