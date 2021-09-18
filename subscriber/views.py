from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #executed when got a request
    return HttpResponse('Empty cite (for now)')
