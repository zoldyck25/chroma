from django.core.checks.messages import Error
from django.http.response import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.urls.resolvers import LocaleRegexDescriptor
from polls.models import polls,Like,Postcomment
from .forms import CreatePollForm
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views import View
from django.urls import reverse,reverse_lazy
from django.http import HttpResponseRedirect


# Create your views here.

def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST, request.FILES )
        if form.is_valid():
            form.save()
            print(form.cleaned_data['title'])
            return redirect('home')    
    form=CreatePollForm()
    params={
        'form':form
    }
    
    return render (request, 'create.html',params)


def like_post(request,mypost_id):
    user = request.user
    if request.method =="POST":
        myposts_id=request.POST.get('mypost_id')
        mypost= polls.objects.get(id=mypost_id)
        
    if user in mypost.liked.all():
        mypost.liked.remove(user)
    else:
        mypost.liked.add(user)
   

    like, created = Like.objects.get_or_create(user=user,post_id=mypost_id)

    if not created:
        if like.value=='Like':
            like.value=='Unlike'
        else:
            like.value='Like'       
    like.save()
    return redirect('/')



def comment(request,mypost_id):
    if request.method =="POST":
        comment =request.POST.get("comment")
        user =request.user 
        postSno= request.POST.get("mypost_id")
        mypost = polls.objects.get(id=mypost_id)
        

        words = {'bad','not good','stupid','crap'}
        if comment in words:
          print(" comment not posted ")
          return redirect('/')
        else:    
         comment = Postcomment(comment=comment,user=user,post=mypost) 
         print("comment posted")
         comment.save() 
        
    
    comments = Postcomment.objects.filter(post=mypost_id)
    myposts =polls.objects.get(id=mypost_id)
    param = {
    "comments":comments,
    'myposts':myposts
    }
    return render  (request,'comment.html',param)


