from django import forms
from django.core.exceptions import ValidationError

#self defined
from Slice.forms import BootstrapModelForm, BootstrapForm
from Pledge.models import Commitment

#inherit Bootstrapform
class CommitmentForm(BootstrapModelForm):

    '''
        Defines the Meta data of your form here. (See your models.py)
    '''
    class Meta:
        model = Commitment
        fields = ['units',
                  'requests',
                 ]

        # If you want to override the default label names
        # e.g 'short_desc' is going to be rendered as "Short desc"
        # if you don't override it
        labels = {
                'requests': 'Special requests',
        }

        #overrides the default charfield for description. Make it a TextArea in HTML as
        #opposed to <input> </input>
        widgets = {
            'requests': forms.Textarea(attrs={
                'cols':50, 'rows':5,
                'class':'form-control'
            }),
        }


