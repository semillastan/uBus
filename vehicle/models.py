# vehicle/models.py
from django.db import models

class Facilities(models.Model):
    facility = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s' % self.facility

class Vehicle_model(models.Model):
    name = models.CharField(max_length=30)
    capacity = models.PositiveIntegerField()
    facilities = models.ManyToManyField(Facilities)

    def __unicode__(self):
        return u'%s' % self.name

class Vehicle(models.Model):
    model = models.ForeignKey(Vehicle_model)
    number = models.PositiveIntegerField()

    def __unicode__(self):
        return u'%s' % self.number


    
