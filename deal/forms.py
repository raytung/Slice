from django import forms
from django.core.exceptions import ValidationError
import datetime



#self defined
from Slice.forms import BootstrapModelForm, BootstrapForm
from deal.models import Deal, Category, Rating
from django.utils import timezone

#inherit Bootstrapform
class CreateDealForm(BootstrapModelForm):
    start_date = forms.DateTimeField(input_formats=['%d/%m/%Y',
                                              '%d/%m/%Y %H:%M',
                                              '%d-%m-%Y',
                                              '%d-%m-%Y %H:%M'])

    end_date = forms.DateTimeField(input_formats=['%d/%m/%Y',
                                              '%d/%m/%Y %H:%M',
                                              '%d-%m-%Y',
                                              '%d-%m-%Y %H:%M'])

    '''
        Defines the Meta data of your form here. (See your models.py)
    '''
    class Meta:
        model = Deal
        fields = ['title',
                  'short_desc',
                  'description',
                  'features_benefits',
                  'category',
                  'cost_per_unit',
                  'num_units',
                  'savings_per_unit',
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
                'min_pledge_amount': 'Minimum total number of pledges',
                'features_benefits': 'Features and benefits',
        }

        error_messages = {
                'start_date':{'invalid': 'Invalid date format. Make sure it is in dd/mm/yyyy'},
                'end_date'  :{'invalid': 'Invalid date format. Make sure it is in dd/mm/yyyy'},
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

    def clean(self):
        cleaned_data = super(CreateDealForm, self).clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        now = timezone.now()
        if start_date < now:
            self._errors['start_date'] = self.error_class([ 'Start date cannot be earlier than now'])
        elif end_date < now:
            self._errors['end_date'] = self.error_class([ 'End date cannot be earlier than now'])
        elif end_date < start_date:
            self._errors['end_date'] = self.error_class(['End date cannot be earlier than start date'])
            self._errors['start_date'] = self.error_class(['End date cannot be earlier than start date'])
        return cleaned_data


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
