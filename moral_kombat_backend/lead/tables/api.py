from rest_framework import viewsets, permissions
from tables.models import *
from .serializer import DemographicsSerializer, StudentSerializer, ProfessorSerializer, ScenariosSerializer, Choices_forSerializer, Stakeholder_pageSerializer, StakeholdersSerializer, ConversationsSerializer, Stakeholder_inSerializer

class DemographicsViewSet(viewsets.ModelViewSet):
    queryset = DEMOGRAPHICS.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DemographicsSerializer

class StudentsViewSet(viewsets.ModelViewSet):
    queryset = STUDENTS.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StudentSerializer

class ProfessorsViewSet(viewsets.ModelViewSet):
    queryset = PROFESSORS.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProfessorSerializer

class StudentTimesViewSet(viewsets.ModelViewSet):
    queryset = STUDENT_TIMES.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StudentTimesSerializer

class ScenariosViewSet(viewsets.ModelViewSet):
    queryset = SCENARIOS.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = ScenariosSerializer

# Choices_For ViewSet
class Choices_forViewSet(viewsets.ModelViewSet):
    queryset = CHOICES_FOR.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = Choices_forSerializer

# Stakeholder_page Viewset
class Stakeholder_pageViewSet(viewsets.ModelViewSet):
    queryset = STAKEHOLDER_PAGE.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = Stakeholder_pageSerializer

# Stakeholders ViewSet
class StakeholdersViewSet(viewsets.ModelViewSet):
    queryset = STAKEHOLDERS.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = StakeholdersSerializer

# Conversations ViewSet
class ConversationsViewSet(viewsets.ModelViewSet):
    queryset = CONVERSATIONS.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = ConversationsSerializer

# Stakeholders_in ViewSet
class Stakeholder_inViewSet(viewsets.ModelViewSet):
    queryset = STAKEHOLDER_IN.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = Stakeholder_inSerializer