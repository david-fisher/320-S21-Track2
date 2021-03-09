from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from django.conf import settings
from .views import *
from django.conf.urls import url

#set up connections from view.py to urls

#router = routers.DefaultRouter()
#router.register('api/ViewName', ViewNameViewSet, 'ViewName')

#urlpatterns = [] 

#urlpatterns += router.urls