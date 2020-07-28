from django.contrib import admin
from User.models import User_user


class User_user_admin(admin.ModelAdmin):
    list_display = ('id','user', 'number','sex')
    search_fields = ('number', 'user__username')


admin.site.register(User_user, User_user_admin)
