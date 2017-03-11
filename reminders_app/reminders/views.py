from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
from .models import Reminder
import sys
reload(sys)
sys.setdefaultencoding('utf8')


from .forms import ReminderForm

def reminder_page(request):
    reminders = Reminder.objects.all()
    if request.method == 'POST':

        print  request.POST
        form = ReminderForm(request.POST)


        if form.is_valid():
            form.save()
            print form.cleaned_data['time']
            print form.cleaned_data['title']

            return HttpResponseRedirect(reverse('reminder_home_page'))
        else:
            print form.errors
    else:
        form = ReminderForm()


    return render(request,"reminder-page.html",{'form': form,'reminders':reminders})