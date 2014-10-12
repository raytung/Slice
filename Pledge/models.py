from django.db import models

from deal.models import Deal
from UserProfile.models import Profile

# Create your models here.
class Commitment(models.Model):
    user = models.ForeignKey(Profile)
    deal = models.ForeignKey(Deal)
    units = models.PositiveIntegerField()
    time_commited = models.DateTimeField(auto_now_add=True)
    requests = models.TextField(max_length=200, blank=True)

    #auto_now_add disallow editing in admin mode
    last_modified_date = models.DateTimeField(auto_now=False)

    def __unicode__(self):
        return [self.user, self.deal]
