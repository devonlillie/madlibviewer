from django.contrib import admin

# Register your models here.
from .models import Madlib,Field
admin.site.register(Madlib)
admin.site.register(Field)
