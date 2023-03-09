from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(DumperModels)
admin.site.register(Machines)
admin.site.register(MachinesOperation)
admin.site.register(Manufacturer)
