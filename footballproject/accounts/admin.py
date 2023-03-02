from django.contrib import admin

# Register your models here.
from accounts.models import User_accounts

admin.site.register(User_accounts)