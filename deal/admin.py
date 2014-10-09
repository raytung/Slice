from django.contrib import admin
from deal.models import Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category)

