from django.contrib import admin
from Project.models import BBS_projects
from Project.models import BBS_comments_projects


# Register your models here.
class BBS_projects_admin(admin.ModelAdmin):
    list_display = ('id','title', 'author', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title',)


admin.site.register(BBS_projects, BBS_projects_admin)  # 注册


class BBS_comments_projects_admin(admin.ModelAdmin):
    list_display = ('id','comment', 'author', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('author',)


admin.site.register(BBS_comments_projects, BBS_comments_projects_admin)  # 注册
from django.contrib import admin

# Register your models here.
