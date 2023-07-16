from django.contrib import admin

from .models import Person, Address

admin.site.register([Person, Address])
