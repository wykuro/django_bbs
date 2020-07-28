from django.contrib import admin
from Problem.models import BBS_problems
from Problem.models import BBS_comments_problems


# Register your models here.
class BBS_problems_admin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title',)


admin.site.register(BBS_problems, BBS_problems_admin)  # 注册


class BBS_comments_problems_admin(admin.ModelAdmin):
    list_display = ('id', 'comment', 'author', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('author',)


admin.site.register(BBS_comments_problems, BBS_comments_problems_admin)  # 注册

admin.site.site_titile = "django"
admin.site.site_header = "管理员页面"
