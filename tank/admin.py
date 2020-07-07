from django.contrib import admin
from tank.models import CduConfig
# Register your models here.

class CduConfigAdmin(admin.ModelAdmin):
    list_display = ('connWay','devPath','ipAddr','port','parityCheck')
    list_filter = ('connWay','devPath','ipAddr','port','parityCheck')
    search_fields = ('connWay','devPath','ipAddr','port','parityCheck')


admin.site.site_header = '液冷控制数据后台'
admin.site.register(CduConfig,CduConfigAdmin)
