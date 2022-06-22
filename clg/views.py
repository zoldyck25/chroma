
from django import views
from polls.models import polls
from math import ceil
from django.http.response import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.urls.resolvers import LocaleRegexDescriptor
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views import View
from django.template import Context
from django.urls import reverse,reverse_lazy
from django.http import HttpResponseRedirect
# Create your views here. 

def home(request):
    myposts = polls.objects.all()
    params ={ 'myposts':myposts}
    return render (request, 'home.html', params)
    
def contactus(request):
    return render (request,'contactus.html')
