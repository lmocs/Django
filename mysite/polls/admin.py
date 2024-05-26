from django.contrib import admin

from .models import Question # This is added to add Question objects to admin interface

# Register your models here.
admin.site.register(Question)