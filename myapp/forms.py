from django.forms import ModelForm
from .models import Listing, Profile

class ListingForm(ModelForm):
  class Meta:
    model = Listing
    fields = '__all__'
    exclude = ['host',]


class ProfileForm(ModelForm):
  class Meta:
    model = Profile
    fields = '__all__'
    exclude = ('name' ,)