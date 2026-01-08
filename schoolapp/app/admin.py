from django.contrib import admin
from app.models import CustomUser,School
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(School)