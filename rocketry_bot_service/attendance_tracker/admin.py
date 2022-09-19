"""Admin Site Registration"""
from django.contrib import admin
from .models import Person, Meeting, AttendanceRecord, Guild

# Register your models here.
admin.site.register(Person)
admin.site.register(Meeting)
admin.site.register(AttendanceRecord)
admin.site.register(Guild)
