from rest_framework import viewsets, permissions
from tables.models import *
from .serializer import DemographicsSerializer, StudentSerializer, EditorSerializer, ScenariosSerializer, Choices_forSerializer, Stakeholder_pageSerializer, StakeholdersSerializer, ConversationsSerializer, Stakeholder_inSerializer

class DemographicsViewSet(viewsets.ModelViewSet):
    queryset = demographics.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DemographicsSerializer

class StudentsViewSet(viewsets.ModelViewSet):
    queryset = students.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StudentSerializer

class EditorsViewSet(viewsets.ModelViewSet):
    queryset = editors.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EditorsSerializer


class ScenariosViewSet(viewsets.ModelViewSet):
    queryset = scenarios.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = ScenariosSerializer

# Choices_For ViewSet
class Choices_forViewSet(viewsets.ModelViewSet):
    queryset = choices_for.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = Choices_forSerializer

# Stakeholder_page Viewset
class Stakeholder_pageViewSet(viewsets.ModelViewSet):
    queryset = stakeholder_page.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = Stakeholder_pageSerializer

# Stakeholders ViewSet
class StakeholdersViewSet(viewsets.ModelViewSet):
    queryset = stakeholders.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = StakeholdersSerializer

# Conversations ViewSet
class ConversationsViewSet(viewsets.ModelViewSet):
    queryset = conversations.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = ConversationsSerializer

# Stakeholders_in ViewSet
class Stakeholder_inViewSet(viewsets.ModelViewSet):
    queryset = stakeholder_in.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = Stakeholder_inSerializer