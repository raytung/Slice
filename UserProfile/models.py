from django.db      import models
from account.models import Account #Account table
from deal.models    import Deal    #Deal table

'''
    Reference: https://docs.djangoproject.com/en/dev/ref/models/fields/

    Model: Profile
    ----------------------------------------------------------------------

    Multiplicities:
    - One to one: Account (provided by Pinax)
    - One to many: Deals, Pledges

    Table Attributes: (variable name: description)
    - profile_picture: User can upload their own profile picture.
    - description:     A brief description of the user him/herself
    - mobile_number:   User's mobile number
    - contact_info:    Addition contact information provided by the User

        Following attributes can be found at
        https://docs.djangoproject.com/en/1.4/topics/auth/

        = first_name
        = last_name
        = email
        = username
        = last_login
        = date_join

    Field options: https://docs.djangoproject.com/en/1.6/ref/models/fields/

'''
class ProfileManager(models.Manager):
    def create_profile(self, account_id):
        return self.create(account = account_id)

class Profile(models.Model):
    #User Modifiable
    profile_picture = models.FileField(null=True,
                                       blank=True,
                                       upload_to="UserProfile/static/images/profile")

    description = models.TextField(blank=True,
                                   max_length=1000,
                                   unique=False)

    mobile_number = models.CharField(max_length=20,
                                     unique=False,
                                     blank=True
                                     )

    contact_info = models.TextField(max_length=500,
                                    blank=True
                                    )

    #User not modifiable
    consecutive_incorrect_login_counts = models.PositiveIntegerField(default=0)
    viewing_history = models.ManyToManyField(Deal, through='History')
    bookmarks = models.ManyToManyField(Deal, related_name="bookmarks")

    #Multiplicities
    account = models.OneToOneField(Account, primary_key=True)

    objects = ProfileManager()


class History(models.Model):
    user = models.ForeignKey('UserProfile.Profile')
    deal = models.ForeignKey('deal.Deal')
    view_date = models.DateTimeField(auto_now=True)

