from django.contrib import admin
from groups.models import Friend

# Register your models here.
class FriendAdmin(admin.ModelAdmin):
    list_display=('current_user',)
admin.site.register(Friend,FriendAdmin)