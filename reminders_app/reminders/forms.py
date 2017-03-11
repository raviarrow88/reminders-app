from django import forms
from .models import Reminder
from django.conf import settings
from django.contrib.admin import widgets
from django.contrib.admin.widgets import AdminSplitDateTime,AdminDateWidget


## reference : http://stackoverflow.com/questions/12449603/integrate-calendar-widget-in-django-app

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class ReminderForm(forms.ModelForm):
    # time = forms.DateField(widget = widgets.AdminSplitDateTime)
    class Meta:
        model = Reminder
        fields = ['title','time']
        widgets = {
            'time': forms.widgets.DateTimeInput( attrs={
                'class': 'datetimepicker',
            }),
        }


    class Media:
        css = {"all":("/static/datepicker/jquery.datetimepicker.min.css",)}
        js = ("/static/datepicker/jquery-ui.min.js", "/static/datepicker/jquery.datetimepicker.min.js",)

