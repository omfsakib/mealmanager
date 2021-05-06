from django.contrib import admin
from addbills.models import Bill

# Register your models here.
class BillAdmin(admin.ModelAdmin):
    list_display=('user','bill','date')

admin.site.register(Bill,BillAdmin)