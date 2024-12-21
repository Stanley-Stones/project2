from django.contrib import admin
from . models import Location, Listing, Profile

# Register your models here.

admin.site.register(Location)
admin.site.register(Listing)
admin.site.register(Profile)
