from django.contrib import admin
from Userauths.models import User
# Register your models here.
class UserAdminModel(admin.ModelAdmin):
  list_display = ['username', 'email', 'phone_number', 'first_name', 'last_name']
admin.site.register(User, UserAdminModel)
