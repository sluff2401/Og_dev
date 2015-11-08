from django import forms
from .models import Event, Userdetail
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('event_date', 'event_detail',)
class UserdetailForm(forms.ModelForm):
    class Meta:
        model = Userdetail
        fields = ('user', 'is_schememanager', 'details', 'schememanager')

