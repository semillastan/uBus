# employee/models.py

from django.db import models
from company.models import Company

class Employee_Type(models.Model):
    emp_type = models.CharField(max_length=20, verbose_name="Employee Type")
    bt_can_add_or_delete = models.BooleanField(verbose_name="Can Add/Delete") # for managing busses and trips
    bt_can_edit = models.BooleanField(verbose_name="Can Edit")
    e_can_add_or_delete = models.BooleanField(verbose_name="Can Add/Delete") # for managing employees
    e_can_edit = models.BooleanField(verbose_name="Can Edit")

    def __unicode__(self):
        return u'%s' % self.emp_type

class Employee(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    middle_name = models.CharField(max_length=25)
    age = models.PositiveIntegerField(max_length=2)
    employee_type = models.ForeignKey(Employee_Type)
    company = models.ForeignKey(Company)
    
    def __unicode__(self):
        return u'%s, %s %s' % self.last_name, self.first_name, self.middle_name


