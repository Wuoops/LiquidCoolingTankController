from django.contrib import admin
from .models import sensorModelConfig
from .models import sensorConfigName
from .models import sensorConfig
from .models import sensorCheckout
#设备路径关系Admin
class sensorModelConfigAdmin(admin.ModelAdmin):
    list_display = ('uuid','devName','modelName','remark')
    list_filter = ('uuid','devName','modelName','remark')
    search_fields = ('devName','modelName')


#配置名称关系Admin
class sensorConfigNameAdmin(admin.ModelAdmin):
    list_display = ('uuid','configName','remark')
    list_filter = ('uuid','configName','remark')
    search_fields = ('configName',)


#传感器配置Admin
class sensorConfigAdmin(admin.ModelAdmin):
    list_display = ('sensorConf','sensorId','sensorName','remark')
    list_filter = ('sensorConf','sensorId','sensorName','remark')
    search_fields = ('sensorName',)

#选中的传感器Admin
class checkedAdmin(admin.ModelAdmin):
    list_display = ('modelUUID','configUUID','numOfCheckedModels')
    list_filter = ('modelUUID','configUUID','numOfCheckedModels',)
    # search_fields = ('sensorName',)

admin.site.site_header = '液冷控制数据后台'
admin.site.register(sensorModelConfig,sensorModelConfigAdmin)
admin.site.register(sensorConfigName,sensorConfigNameAdmin)
admin.site.register(sensorConfig,sensorConfigAdmin)
admin.site.register(sensorCheckout,checkedAdmin)
