from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def SignIn(request):
    return HttpResponse('<h3>HttpResponse<h3>')