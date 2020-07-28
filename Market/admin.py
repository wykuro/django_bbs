from django.contrib import admin
from Market.models import BBS_goods


# Register your models here.
class BBS_goods_admin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title',)


admin.site.register(BBS_goods, BBS_goods_admin)  # 注册
