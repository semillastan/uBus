# trip/models.py
from django.db import models
from vehicle.models import Vehicle

class Province(models.Model):
    province = models.CharField(max_length=30)
    
    def __unicode__(self):
        return u'%s' % self.province

class Town(models.Model):
    province = models.ForeignKey(Province)
    town = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s' % self.town

class Trip(models.Model):
    origin = models.ForeignKey(Province, related_name="origin")
    destination = models.ForeignKey(Province, related_name="destination")
    departure = models.DateTimeField()
    eta = models.DateTimeField()
    vehicle_used = models.ForeignKey(Vehicle)

    def __unicode__(self):
        return u'%s - %s' % self.origin, self.destination

