#Django libraries
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import models

#self defined
from deal.forms import BootstrapForm

class EditAccountForm(BootstrapForm):
    class Meta:
        model = models.User
        fields =['first_name',
                 'last_name']
        



