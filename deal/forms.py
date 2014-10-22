from django import forms
from django.core.exceptions import ValidationError



#self defined
from Slice.forms import BootstrapModelForm, BootstrapForm
from deal.models import Deal, Category, Rating

#inherit Bootstrapform
class CreateDealForm(BootstrapModelForm):

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
                'min_pledge_amount': 'Minimum pledging amount'

        }

        error_messages = {
                'start_date':{'invalid': 'Invalid date format. Make sure it is in mm/dd/yyyy'},
                'end_date'  :{'invalid': 'Invalid date format. Make sure it is in mm/dd/yyyy'},
                'cost_per_unit':{'invalid': 'Cost cannot be less than 0!'},
                }

        #overrides the default charfield for description. Make it a TextArea in HTML as
        #opposed to <input> </input>
        widgets = {
            'description': forms.Textarea(attrs={
                'cols':50, 'rows':10,
                'class':'form-control'
            }),
        }

class SearchDealForm(BootstrapForm):
   search = forms.CharField(max_length=100, required=False)

   #min_price & max_price are assumed to be min/max price per unit
   min_price = forms.FloatField(min_value=0.00, required=False)
   max_price = forms.FloatField(min_value=0.00, required=False)

   start_date = forms.DateTimeField(required=False)
   end_date = forms.DateTimeField(required=False)
   category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)

class RateDealForm(BootstrapModelForm):
    class Meta:
        model = Rating
        fields = ['rating']
