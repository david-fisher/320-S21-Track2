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

router.register(r'pages', views.PagesViewSet)
router.register(r'stakeholder_page', views.Stakeholder_pageViewSet)
router.register(r'reflection_questions', views.Reflection_QuestionsViewSet)
router.register(r'generic_page', views.Generic_pageViewSet)
router.register(r'action_page', views.Action_pageViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
