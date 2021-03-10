from django.shortcuts import render
from rest_framework import viewsets
from api.models import *
from api.serializers import *

# Create your views here.
class ScenariosViewSet(viewsets.ModelViewSet):
    queryset= Scenario.objects.all()
    serializer_class = ScenarioSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = Webuser.objects.all()
    serializer_class = UserSerializer

