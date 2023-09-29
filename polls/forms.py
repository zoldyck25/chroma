from django.forms import ModelForm
from django import forms
from .models import polls

class CreatePollForm(ModelForm):
    class Meta:
        model = polls
        fields = 'title','Images','pub_date'
        labels={
            'title':'',
            'Images':'',
            'pub_date':'',
        }  
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','name':'title','placeholder':'Title'} ),
            'Images':forms.FileInput(attrs={'class':'form-control','placeholder':'Choose'}), 
            'pub_date':forms.DateInput(attrs={'class':'form-control','placeholder':'Date'}),
        
        }   
