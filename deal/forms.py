#Django libraries
from django import forms
from django.core.exceptions import ValidationError

#self defined
from deal.models import Deal

#this class sets the class of every widgets into 'form-control'.
#for bootstap styling
class BootstrapForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BootstrapForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

#inherit Bootstrapform
class CreateDealForm(BootstrapForm):
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


