from django.db import models

# Create your models here.
class Deal(models.Model):
    #User modifiable
    title = models.CharField(max_length=128, unique=False)
    description = models.CharField(max_length=1000)
    cost_per_unit = models.DecimalField(max_digits=5, decimal_places=2)
    num_units = models.PositiveIntegerField()
    start_date = models.TimeField(auto_now=False)
    end_date = models.TimeField(auto_now=False)
    '''
        Specifies the state of each deal.
        the first element of each tuple is the actual data stored in the database.

        call the actual string in python by the method .get_state_display()
    '''
    STATE_CHOICES = ( 
            ('CMNG', 'Coming up'),
            ('STRT', 'Started'),
            ('ENDD', 'Ended'),
            ('CNCL','Canceled'),
            ('DLYD', 'Delayed')
            )
    state = models.CharField(max_length=4, choices=STATE_CHOICES)
    delivery_method = models.TextField()
    min_pledge_amount = models.PositiveIntegerField()
    #specifies multiplicity
   # search_tags = models.ManyToManyField("SearchTag")

    #Calculated by the system
    time_posted = models.TimeField()
    #owner_id = models.ForeignKey("User")
    last_modified_date = models.TimeField()
    
    def __unicode__(self):
        return self.title