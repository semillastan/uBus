# trip/admin.py
from django.contrib import admin
from trip.models import Province, Town,Trip

class TownsInline(admin.TabularInline):
    model = Town

class ProvinceAdmin(admin.ModelAdmin):
    fields = ['province']
    inlines = [TownsInline]    

admin.site.register(Province, ProvinceAdmin)
admin.site.register(Trip)
