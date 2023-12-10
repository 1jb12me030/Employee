from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Employee)
admin.site.register(Qualification)
admin.site.register(Project)
admin.site.register(WorkExperience)
admin.site.register(AddressDetails)
