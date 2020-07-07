from django.contrib import admin
from .models import NodeInfo,BmcConfName,BmcCheckoutConf,BmcConfig

#设备路径关系Admin
class NodeInfoAdmin(admin.ModelAdmin):
    list_display = ('nodeName','nodeIP','nodeIpBmc','nodeMac','bmcUserName','bmcPassword','nodeStatus','remark')
    list_filter = ('nodeName','nodeIP','nodeIpBmc','nodeMac','bmcUserName','bmcPassword','nodeStatus','remark')
    search_fields = ('nodeName','nodeIP','nodeIpBmc','nodeMac','bmcUserName','bmcPassword','nodeStatus','remark')



class BmcConfNameAdmin(admin.ModelAdmin):
    list_display = ('uuid','confName','remark')


class BmcCheckoutConfAdmin(admin.ModelAdmin):
    list_display = ('nodeid','bmcConfId')


class BmcConfigAdmin(admin.ModelAdmin):
    list_display = ('uuid','confId','keyword','description','remark')


admin.site.site_header = '液冷控制数据后台'
admin.site.register(NodeInfo,NodeInfoAdmin)
admin.site.register(BmcConfName,BmcConfNameAdmin)
admin.site.register(BmcCheckoutConf,BmcCheckoutConfAdmin)
admin.site.register(BmcConfig,BmcConfigAdmin)
