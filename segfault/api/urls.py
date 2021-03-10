from django.urls import path, include
from rest_framework import routers

from api import *

# Create a router and register our viewsets with it.
router = routers.DefaultRouter()

#router.register(, views.SnippetViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]