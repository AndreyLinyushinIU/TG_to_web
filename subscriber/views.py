from django.http import HttpResponse
from django.shortcuts import render
from subscriber.models import User

def index(request):
    #executed when got a request
    #User(usr='Andruxa', password='yopta_blya').save()
    #print(User.objects.filter(usr='Andruxa'))
    #print('aaaaaaaaaaaaa\n')
    #return HttpResponse('Empty cite (for now)')
    return render(request, 'index.html', {})
