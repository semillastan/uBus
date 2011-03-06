# vehicle/admin.py
from django.contrib import admin

from vehicle.models import Vehicle, Facilities, Vehicle_model

admin.site.register(Vehicle)
admin.site.register(Vehicle_model)
admin.site.register(Facilities)
