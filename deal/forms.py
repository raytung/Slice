#Django libraries
from django import forms, ModelForm
from django.core.exceptions import ValidationError

#self defined
from deal.models import Deal

class CreateDealForm(forms.ModelForm):
    
    
