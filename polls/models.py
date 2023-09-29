from django.db import models
from django.db.models.fields.related import ForeignKey
from django.urls import reverse
from django.utils.timezone import now
from  django.contrib.auth.models import User


# Create your models here.

class polls(models.Model):
    title=models.TextField(max_length=50)
    Images=models.ImageField(upload_to='clg/images/', default="")
    pub_date=models.DateField(null=True) 
    liked=models.ManyToManyField(User, default=None,blank=True,related_name='liked')   
    def __str__(self):
        return str (self.title)

@property
def num_likes(self):
    return self.liked.all().count()    

LIKE_CHOICES ={
      ('Like','Like'),
      ('Unlike','Unlike'),
}

class Like(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(polls,on_delete=models.CASCADE)
    value=models.CharField(choices=LIKE_CHOICES,default='Like', max_length=10)
    
    def __str__(self):
     return str(self.post) 

class Postcomment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(polls,on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,null=True)
    timestamp= models.DateTimeField(default=now) 

