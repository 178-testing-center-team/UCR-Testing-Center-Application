from django.contrib import admin
from .models import Account

#admin.site.register(Account)


class AccountAdmin(admin.ModelAdmin):
    list_display = ("__str__", "user_type")
    
admin.site.register(Account, AccountAdmin)