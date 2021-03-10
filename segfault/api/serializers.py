from rest_framework import serializers
from api.models import *

#TODO: Need to disable after depolying(security)
class ScenarioSerializer(serializers.Serializer):
    class Meta:
        model = Scenario
        fields = ['id','name','date_created']
    
    
#TODO: Need to disable after depolying(security)
class UserSerializer(serializers.HyperlinkedModelSerializer):
    

    class Meta:
        model = Webuser
        fields = ['url','id','username']
    

