from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Member)
admin.site.register(Contact)
admin.site.register(Profile)
