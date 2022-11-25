from django.contrib import admin

# Register your models here.
from accounts.models import Account, Subs

admin.site.register(Account)

admin.site.register(Subs)

