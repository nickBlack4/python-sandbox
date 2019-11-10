from django.urls import path
from . import views

# movies/
# movies/1/details

# set to a list, convention Django expects us to follow

"""
    we define this variable urlpatterns that contains one or
    more path object that map url endpoints to view functions

    refer to this as a url configuration.  Every app should have a url configuration.
"""
urlpatterns = [
    path('', views.index, name='index')
]
