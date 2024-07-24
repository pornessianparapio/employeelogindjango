from django.contrib import admin
from .models import Employee, Activity, TimeEntry

admin.site.register(Employee)
admin.site.register(Activity)
admin.site.register(TimeEntry)
