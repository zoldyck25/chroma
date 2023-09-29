from django.contrib import admin
from django.urls import path,include
from django.urls.conf import include

from  . import views




urlpatterns = [
   path('create/',views.create,name='create'),
   path('like_post/<mypost_id>/',views.like_post,name='like_post'),
   path('comment/<mypost_id>/',views.comment,name='comment'),

 
] 