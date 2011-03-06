# employee/admin.py

from django.contrib import admin
from employee.models import Employee, Employee_Type

class EmployeeTypeAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields':['emp_type']}),
        ('Employees Management', {'fields': ['e_can_add_or_delete', 'e_can_edit']}),
        ('Bus/Trip Management', {'fields': ['bt_can_add_or_delete', 'bt_can_edit']}),
    )

admin.site.register(Employee)
admin.site.register(Employee_Type, EmployeeTypeAdmin)
