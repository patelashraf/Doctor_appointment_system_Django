import imp
from django.contrib import admin
from authenticate_me.models import *
# Register your models here.

admin.site.register(User_reg)
admin.site.register(dr_reg)
admin.site.register(User)

# admin.site.register(Profile)