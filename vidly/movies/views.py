from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

"""
    a view function is a function that takes a request and returns a response
"""

"""
    mvc -- Django has variation of this pattern model view template.

    the views in Django are like Controllers in MVC
"""

# usually use the word index for naming the function that represents the main page of the app

def index(request):
    # return http response
    return HttpResponse("Hello World")