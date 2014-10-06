from django import forms
from django.core.exceptions import ValidationError

#this class sets the class of every widgets into 'form-control'.
#for bootstap styling
class BootstrapForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(BootstrapForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


