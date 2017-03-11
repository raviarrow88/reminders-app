from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
# Create your models here.

class Reminder(models.Model):
    title = models.CharField(max_length=250,default=None,null=True,blank=False)
    time = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now=False,auto_now_add=True)
    created_by = models.ForeignKey(User,default=None,null=True)
