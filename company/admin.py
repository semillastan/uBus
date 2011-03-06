# company/admin.py
from django.contrib import admin
from company.models import Company, Company_contact_information
from employee.models import Employee

class ContactInfoInLine(admin.TabularInline):
    model = Company_contact_information

class EmployeeInline(admin.TabularInline):
    model = Employee

class CompanyAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Company Information', {'fields':['company_type','name', 'address','business_permit']}),
    ]
    inlines = [ContactInfoInLine, EmployeeInline]

admin.site.register(Company, CompanyAdmin)

