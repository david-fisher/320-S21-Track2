from django.urls import path, include
from rest_framework import routers
from api import views

# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r'scenarios', views.ScenariosViewSet)   
router.register(r'courses', views.CourseViewSet)
router.register(r'professors', views.ProfessorViewSet)
router.register(r'students', views.StudentViewSet)
router.register(r'demographics', views.DemographicViewSet)

router.register(r'issues', views.IssueViewSet)
router.register(r'conversations', views.ConversationsViewSet)
router.register(r'responses', views.ResponsesViewSet)

router.register(r'pages', views.PagesViewSet)
router.register(r'stakeholder_to_page', views.Stakeholder_to_pageViewSet)
router.register(r'reflection_questions', views.Reflection_QuestionsViewSet)
router.register(r'generic_page', views.Generic_pageViewSet)
router.register(r'action_page', views.Action_pageViewSet)

router.register(r'reflections_taken', views.ReflectionsTakenViewSet)
router.register(r'response_to_action_page', views.ResponseToActionPageViewSet)
router.register(r'responses_to_conversations', views.Responses_to_conversationsViewSet)
router.register(r'student_times', views.StudentTimesViewSet)
router.register(r'student_page_progress',views.Student_page_progressViewSet)

router.register(r'coverage', views.CoverageViewSet)
router.register(r'stakeholders', views.StakeholdersViewSet)

#TODO: register apiviews to api_root view(there are only viewsets now)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('dashboard/',views.DashBoard.as_view()),
    path('get_scenario/', views.Get_scenario.as_view()),
    path('get_pages/',views.get_pages.as_view()),
]
