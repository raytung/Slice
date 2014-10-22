from django.db    import models
from datetime     import datetime
from django.utils import timezone

# https://docs.djangoproject.com/en/dev/ref/validators/#minvaluevalidator
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

'''
    Reference: https://docs.djangoproject.com/en/dev/ref/models/fields/

    Model: Deal
    ----------------------------------------------------------------------

    Multiplicities:
    - Many To Many: Search Tag, UserProfile


    Table Attributes: (variable name: description)
    - title:           The title of the Deal
    - short_desc:      A short description of the Deal. Will be displayed
                       search result
    - description:     A brief description of the Deal
    - cost_per_unit:   Price per unit of item
    - num_units:       The number of available units in the Deal
    - start_date:      The start date of the Deal
    - end_date:        The end date of the Deal
    - state:           The state of the Deal. There are 4 states.
                        -> Coming Up: The deal has not started yet
                        -> Started:   The deal has started, but has not reached end date
                        -> Ended:     The deal has reached end date
                        -> Canceled:  The deal has been cancelled by the owner
                        -> Delayed:   The owner has chose to delay the start date
    - category:        The category of each deal.
    - delivery_method: Owner must specific the delivery method for the items
    - min_pledge_amount: The minimum commitment number of units
    - time_posted:     The time the Deal has been posted
    - last_modified_date: The latest modified date of the deal.

    Field options: https://docs.djangoproject.com/en/1.6/ref/models/fields/

    Last modified by: Ray Tung 20/09/2014
'''


class Deal(models.Model):
    #User modifiable
   title = models.CharField(max_length=128, unique=False)
   short_desc = models.CharField(max_length=200, default=" ")
   description = models.TextField(max_length=800)
   features_benefits = models.TextField(max_length=500, default= " ")
   #decimal field as opposed to floatfield http://stackoverflow.com/questions/2569015/django-floatfield-or-decimalfield-for-currency
   cost_per_unit = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0.00)])
   num_units = models.PositiveIntegerField()
   available_units = models.PositiveIntegerField()
   savings_per_unit = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0.00)])
   start_date = models.DateTimeField(auto_now=False, help_text="MM/DD/YYYY hh:mm")
   end_date = models.DateTimeField(auto_now=False, help_text="MM/DD/YYYY hh:mm")
   '''
       Specifies the state of each deal.
       the first element of each tuple is the actual data stored in the database.

       call the actual string in python by the method .get_state_display()
   '''
   STATE_CHOICES = (
            ('CMNG', 'Coming up'),
            ('STRT', 'Started'),
            ('ENDD', 'Ended'),
            ('CNCL', 'Canceled'),
            ('DLYD', 'Delayed')
            )
   state = models.CharField(max_length=4,
            choices=STATE_CHOICES)

   delivery_method   = models.TextField()
   min_pledge_amount = models.PositiveIntegerField()

    #Multiplicities
   search_tags = models.ManyToManyField("SearchTag")
   category = models.ForeignKey('deal.Category')
   owner = models.ForeignKey("UserProfile.Profile")

    #User not modifiable
   time_posted = models.DateTimeField(auto_now=True)
   last_modified_date = models.DateTimeField(auto_now=True)

   def __unicode__(self):
       return self.title

    #overriding the default save method.

   def save(self, *args, **kwargs):
       if   self.start_date > timezone.now():
           self.state = "CMNG"
       elif self.start_date < timezone.now():
           self.state = "STRT"
       elif self.end_date <= timezone.now():
           self.state = "ENDD"

        #start date cannot be later than end date. Does not save.
       if self.start_date >= self.end_date:
           return

       super(Deal, self).save(*args, **kwargs)


class SearchTag(models.Model):
    tag_name = models.CharField(max_length=20,
            unique=True)

    def __unicode__(self):
        return self.tag_name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.name

class Rating(models.Model):
    rating = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    deal = models.ForeignKey("deal.Deal")
    user = models.ForeignKey("UserProfile.Profile", related_name="current_user")
    #use Queryset.objects.get_or_create() or else user can rate many times

    def __unicode__(self):
        return self.rating
