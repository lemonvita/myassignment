from django.contrib import admin

from app.models import Person, Address

admin.site.register([Person, Address])
