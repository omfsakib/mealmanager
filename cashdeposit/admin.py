from django.contrib import admin
from cashdeposit.models import CashDeposit

# Register your models here.
class CashDepositAdmin(admin.ModelAdmin):
    list_display=('user','cashdeposit','date')
admin.site.register(CashDeposit,CashDepositAdmin)