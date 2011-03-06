# company/models.py
from django.db import models

class Company(models.Model):
    COMPANY_TYPE = (
        (u'M', u'Main'),
        (u'B', u'Branch'),
    )
    name = models.CharField(max_length=30, unique=True)
    address = models.CharField(max_length=150)
    business_permit = models.PositiveIntegerField(unique=True)
    company_type = models.CharField(max_length=2, choices=COMPANY_TYPE)
    
    
    def __unicode__(self):
        return u'%s' % self.name

class Company_contact_information(models.Model):
    CONTACT_TYPE = (
        (u'L', u'Landline'),
        (u'M', u'Mobile'),
        (u'E', u'Email'),
    )
    company = models.ForeignKey(Company)
    contact_type = models.CharField(max_length=1, choices=CONTACT_TYPE)
    contact_detail = models.CharField(max_length=25)

    def __unicode__(self):
        return u'%s : %s' % self.contact_type, self.contact_details
