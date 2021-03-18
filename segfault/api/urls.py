from django.urls import path, include
from rest_framework import routers
from api import views

# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r'scenarios', views.ScenariosViewSet)   
router.register(r'courses', views.CoursesViewSet)
router.register(r'demographic', views.DemographicViewSet)
router.register(r'issues', views.IssuesViewSet)
router.register(r'conversations', views.ConversationsViewSet)
router.register(r'responses', views.ResponsesViewSet)
router.register(r'scenarios_for', views.Scenarios_forViewSet)
router.register(r'coverage', views.CoverageViewSet)
router.register(r'stakeholders', views.StakeholdersViewSet)
# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
