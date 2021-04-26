from django.db import models
from django.utils import timezone
from accounts.models import User
import datetime
class User_Attributes(models.Model):
    SEX = (
        ('F', 'Female'),
        ('M', 'Male'),
    )
    date_posted = models.DateTimeField(default=timezone.now)
    details_filled = models.BooleanField(default=False)
    age = models.IntegerField()
    pneumonia = models.BooleanField(default=False)
    gender = models.CharField(
        max_length=1,
        choices=SEX,

    )
    #user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    user = models.IntegerField(default='1')
    obesity = models.BooleanField(default=False)
    breathing = models.BooleanField(default=False)
    pregnant = models.BooleanField(default=False)
    smoker = models.BooleanField(default=False)
    diabetic = models.BooleanField(default=False)
    ckd = models.BooleanField(default=False)
    copd = models.BooleanField(default=False)
    immunocompromised = models.BooleanField(default=False)
    heart = models.BooleanField(default=False)
    asthma = models.BooleanField(default=False)
    blood = models.BooleanField(default=False)
    others = models.BooleanField(default=False)
    #def __str__(self):
     #   a=User.objects.filter(id=self.user)[0]
      #  return a.username

class Hospital(models.Model):
    admin=models.IntegerField(default='1')
    name = models.CharField(max_length=100)
    address =  models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    available_Vaccine = models.IntegerField()
    que= models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Request_Manager(models.Manager):
    def create_data(self, user,hospital,priority,fulfilled,confirmtime):
        details = self.create(user=user,hospital=hospital,time=datetime.datetime.now(),priority=priority,fulfilled=fulfilled,confirmtime=confirmtime)
        return details

class Request(models.Model):
    user = models.IntegerField()
    hospital = models.IntegerField()
    time = models.DateTimeField()
    priority = models.FloatField()
    fulfilled = models.BooleanField()
    confirmtime = models.CharField(max_length=50)
    objects = Request_Manager()
    #def __str__(self):
     #   a=User.objects.filter(id=self.user)[0]
      #  return a.username
