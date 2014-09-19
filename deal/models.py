from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Deal(models.Model):
    #User modifiable
    title = models.CharField(max_length=128, unique=False)
    short_desc = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    cost_per_unit = models.DecimalField(max_digits=5, decimal_places=2)
    num_units = models.PositiveIntegerField()
    start_date = models.DateTimeField(auto_now=False)
    end_date = models.DateTimeField(auto_now=False)
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
    state = models.CharField(max_length=4, choices=STATE_CHOICES)

    CATEGORIES = (
            ('ARTT', 'Art'),
            ('BABY', 'Baby Products'),
            ('BOOK', 'Books'),
            ('ELEC', 'Electronics and Cameras'),
            ('COMP', 'Computers'),
            ('ENTM', 'Entertainment'),
            ('TOYS', 'Toys and Collectables'),
            ('CLTH', 'Clothes and Fashion'),
            ('FOOD', 'Food')
            )

    category = models.CharField(max_length=4, choices=CATEGORIES)

    delivery_method = models.TextField()
    min_pledge_amount = models.PositiveIntegerField()
    
    #specifies multiplicity
    search_tags = models.ManyToManyField("SearchTag")

    #Calculated by the system
    time_posted = models.DateTimeField(auto_now=True)
    #owner_id = models.ForeignKey("User")
    last_modified_date = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.start_date > timezone.now():
            self.state = "CMNG"
        elif self.start_date < timezone.now():
            self.state = "STRT"
        elif self.end_date <= timezone.now():
            self.state = "ENDD"
        
        if self.start_date >= self.end_date: # start date cannot be later than end date
            return

        super(Deal, self).save(*args, **kwargs)

class SearchTag(models.Model):
    tag_name = models.CharField(max_length=20, unique=True)

    def __unicode__(self):
        return self.tag_name


