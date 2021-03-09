from rest_framework import serializers
from .models import *

#taken from last semester's editor backend

#class ScenariosSerializer(serializers.ModelSerializer):
    #class Meta:
        #model = scenarios
        #fields = ('SCENARIO', 'VERSION', 'NAME', 'IS_FINISHED', 'PUBLIC', 'NUM_CONVERSATION', 'PROFESSOR')