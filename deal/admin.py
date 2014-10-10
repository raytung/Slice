from django.contrib import admin
from deal.models import Deal

class DealAdmin(admin.ModelAdmin):
    fields = ('title', 'short_desc', 'description', 'start_date', 'end_date', 'cost_per_unit', 'num_units', 'state', 'delivery_method', 'min_pledge_amount', 'owner'  )
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        obj.save()

# Register your models here.

admin.site.register(Deal, DealAdmin)

