from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist


#Pinax
from account.models import Account

#Models
from UserProfile.models import Profile

def index(request):
    # Force create user profile on login (if profile not found)
    if request.user.is_authenticated():
        try:
            profile = Profile.objects.get(account_id=request.user.id)
        except ObjectDoesNotExist:
            user_account = Account.objects.get(user_id=request.user.id)
            profile = Profile.objects.create_profile(user_account)
    return render(request, 'homepage.html', {})

