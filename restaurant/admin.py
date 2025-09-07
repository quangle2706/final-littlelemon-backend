from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.
from .models import Menu
from .models import Booking


admin.site.register(Menu)
admin.site.register(Booking)