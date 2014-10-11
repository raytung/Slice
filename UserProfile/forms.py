#Django libraries
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import models
from UserProfile.models import Profile

#self defined
from deal.forms import BootstrapModelForm

class EditAccountForm(BootstrapModelForm):
    class Meta:
        model = models.User
        fields =['first_name',
                 'last_name']
        
class EditDescriptionForm(BootstrapModelForm):
	class Meta:
		model = Profile
		fields = ['description']

class EditContactForm(BootstrapModelForm):
	class Meta:
		model = Profile
		fields = ['mobile_number',
				  'contact_info']
