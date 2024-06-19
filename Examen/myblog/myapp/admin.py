from django.contrib import admin
from .models import flight
from .models import train
from .models import cruise


# Register your models here.
admin.site.register(flight)
admin.site.register(train)
admin.site.register(cruise)