import datetime
from django.db                              import models
from django.utils                           import timezone
from django.contrib.auth.models             import User


class Userdetail(models.Model):
  user                = models.OneToOneField('auth.User')
  is_schememanager    = models.BooleanField(default=False)
  details             = models.TextField(blank=True,null=True)
  schememanager       = models.ForeignKey('auth.User', related_name='scheme_manager',blank=True,null=True)
  def __str__(self):               
    return str(self.user)

class Event(models.Model):
  author            = models.ForeignKey(Userdetail)
  author_name       = models.CharField(max_length=20,default="schememanager")
  event_date        = models.DateField('Event date in the format yyyy-mm-dd, e.g for the 24th of August 2015, enter 2015-08-24', max_length=10)
  schememanager     = models.ForeignKey(Userdetail, related_name='post_scheme_manager',blank=True,null=True)
  event_detail      = models.TextField('Event details')
  created_date      = models.DateTimeField(default=timezone.now)
  is_live           = models.BooleanField(default=True)
  def __str__(self):               
    return self.event_detail
  def publish(self):
    self.save()

  
