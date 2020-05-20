from django.db import models
from django.utils import timezone
from django.urls import reverse
import pytz
# Create your models here.

TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
# Create your models here.
class User_Name(models.Model):
    id = models.AutoField(primary_key=True)
    real_name = models.CharField(max_length=20)
    timezone = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')


class Time_Period(models.Model):
    user_name = models.ForeignKey(User_Name, related_name='activity_periods', on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
