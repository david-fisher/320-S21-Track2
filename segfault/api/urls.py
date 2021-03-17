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


# response, reflections_taken, response_to_action_page, conversations_had, student_times
router.register(r'reflections_taken', views.ReflectionsTakenViewSet)
router.register(r'response_to_action_page', views.ResponseToActionPageViewSet)
router.register(r'conversations_had', views.ConversationsHadViewSet)
router.register(r'student_times', views.StudentTimesViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
