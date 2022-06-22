from django.contrib import admin
from . models import polls,Like,Postcomment

# Register your models here.

admin.site.register(polls)
admin.site.register(Like)
admin.site.register(Postcomment)

