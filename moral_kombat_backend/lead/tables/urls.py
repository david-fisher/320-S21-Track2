from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from django.conf import settings
from .views import *
from django.conf.urls import url

# DemographicsViewSet, allScenariosViewSet, StudentsViewSet, ProfessorsViewSet, ScenariosViewSet, Choices_forViewSet, Stakeholder_pageViewSet, ConversationsViewSet, Stakeholder_inViewSet, StakeholdersViewSet

router = routers.DefaultRouter()
router.register('api/demographics', DemographicsViewSet, 'demographics') #
router.register('api/students', StudentsViewSet, 'students') #
router.register('api/professors', ProfessorsViewSet, 'professors') #
router.register('api/scenarios', ScenariosViewSet, 'scenarios') #
router.register('api/pages', PagesViewSet, 'pages') #
#router.register('api/stakeholder_page', Stakeholder_pageViewSet, 'stakeholder_page')
router.register('api/reflection_questions', Reflection_QuestionsViewSet, 'reflection_questions') 
# #ref q to page, page to scenario, stake to page, respon to conver, courses to scen
#students to course, prof to scen, respone to action page, assigned to, student times

router.register('api/reflection_question_to_page', Reflection_Question_to_pageViewSet, 'reflection_question_to_page')
#router.register('api/pages_to_scenario', PagesToScenarioSerializer, 'pages_to_scenario')
router.register('api/stakeholder_to_page', Stakeholder_pageViewSet, 'stakeholder_to_page')
router.register('api/responses_to_conversations', Responses_to_ConversationsViewSet, 'responses_to_conversations')
# router.register('api/stakeholders', StakeholdersViewSet, 'stakeholders')
# router.register('api/stakeholders', StakeholdersViewSet, 'stakeholders')
# router.register('api/stakeholders', StakeholdersViewSet, 'stakeholders')
# router.register('api/stakeholders', StakeholdersViewSet, 'stakeholders')
# router.register('api/stakeholders', StakeholdersViewSet, 'stakeholders')
# router.register('api/stakeholders', StakeholdersViewSet, 'stakeholders')

router.register('api/stakeholders', StakeholdersViewSet, 'stakeholders') #
router.register('api/conversations', ConversationsViewSet, 'conversations') #
router.register('api/reflectionstaken', ReflectionsTakenViewSet, 'reflectionstaken') #
#router.register('api/conversationshad', ConversationsHadViewSet, 'conversationshad') #
#router.register('api/studentsin', StudentsInViewSet, 'studentsin')
router.register('api/courses', CoursesViewSet, 'courses') #
router.register('api/responses', ResponsesViewSet, 'responses') #
router.register('api/scenarios_for', Scenarios_forViewSet, 'scenarios_for') #
router.register('api/generic_page', generic_pageViewSet, 'generic_page') #
#router.register('api/professors_teach', Professors_teachViewSet, 'professors_teach') #professors to courses
#router.register('api/single_scenario', SingleScenarioViewSet, 'single_scenario')
router.register('api/issues', IssuesViewSet, 'issues') #
router.register('api/action_page', Action_pageViewSet, 'action_page') #
router.register('api/coverage', CoverageViewSet, 'coverage') #
#router.register('api/actions_taken',ActionsTakenViewSet,'actions_taken')


urlpatterns = [
    # path('allScenarios', allScenariosViewSet.as_view()),
    # path('multi_conv', multi_conv.as_view()),
    # path('multi_stake', multi_stake.as_view()),
    # path('multi_coverage', multi_coverage.as_view()),
    # path('logistics', logistics_page.as_view()),
    # path('multi_issue', multi_issue.as_view()),
    # path('dashboard', dashboard_page.as_view()),
    # path('flowchart', flowchart.as_view()),
    # path('student_info',student_info.as_view()),
    # path('student_responses',student_responses.as_view()),

    # path('coverages', coverages_page.as_view()),
    # path('stakeholder', stakeholders_page.as_view()),
    # path('coverages', coverages_page.as_view()),
    # path('page', pages_page.as_view()),

] 

urlpatterns += router.urls