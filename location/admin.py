from django.conf import settings
from django.contrib import admin

from .models import Location

admin.site.site_header = settings.PROJECT_NAME.title()
admin.site.site_title = settings.PROJECT_NAME.title() + "后台管理"


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):

    title = "xxx"
    # 设置列表可显示的字段
    list_display = ("create_time", "class_name", "func_name", "args", "sys_arch", "px", "location_x", "location_y")
    #
    fields = ("class_name", "func_name", "args", "sys_arch", "px", "location_x", "location_y")