from django.forms import ModelForm

from .models import polls

class CreatePollForm(ModelForm):
    class Meta:
        model = polls
        fields = 'title','Images','pub_date'
      
