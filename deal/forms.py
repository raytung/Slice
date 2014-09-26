from django import forms
from django.core.exceptions import ValidationError


#self defined
from Slice.forms import BootstrapForm
from deal.models import Deal

#inherit Bootstrapform
class CreateDealForm(BootstrapForm):

    '''
        Defines the Meta data of your form here. (See your models.py)
    '''
    class Meta:
        model = Deal
        fields = ['title',
                  'short_desc',
                  'description',
                  'category',
                  'cost_per_unit',
                  'num_units',
                  'start_date',
                  'end_date',
                  'delivery_method',
                  'min_pledge_amount',
                  ]

        # If you want to override the default label names
        # e.g 'short_desc' is going to be rendered as "Short desc"
        # if you don't override it
        labels = {
                'short_desc': 'Short description',
                'num_units': 'Units available',
                'min_pledge_amount': 'Minimum Pledging Units'

        }

        #overrides the default charfield for description. Make it a TextArea in HTML as
        #opposed to <input> </input>
        widgets = {
            'description': forms.Textarea(attrs={
                'cols':50, 'rows':10,
                'class':'form-control'
            }),
        }


