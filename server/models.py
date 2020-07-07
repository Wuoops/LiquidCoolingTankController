from django.db import models

#server信息
class NodeInfo(models.Model):

    uuid = models.AutoField(primary_key=True,verbose_name='自增主键')
    nodeName = models.CharField(max_length=128 ,verbose_name='节点名称')
    nodeIP = models.CharField(max_length=128,verbose_name='节点IP地址')
    #在testing分支作修改尝试
    nodeIpBmc = models.CharField(max_length=128,verbose_name='BMC IP地址')
    nodeMac = models.CharField(max_length=128,verbose_name='节点MAC地址')
    bmcUserName = models.CharField(max_length=128,verbose_name='BMC帐号')
    bmcPassword = models.CharField(max_length=128,verbose_name='BMC密码')
    nodeStatus = models.IntegerField(verbose_name='节点运行状态码(0：关机，1：运行中，2：标记运行,3：标记关机,4：其他标记)')
    remark = models.TextField(verbose_name='备注',help_text='备注信息')

    class Meta:
        verbose_name = verbose_name_plural = 'SERVER信息表'


#BMC配置名称表
class BmcConfName(models.Model):
    uuid = models.AutoField(primary_key=True,verbose_name='自增主键')
    confName = models.CharField(max_length=128,verbose_name='配置名称')
    remark = models.TextField(verbose_name='备注',help_text='备注信息')

    class Meta:
        verbose_name = verbose_name_plural = '配置名称表'

#BMC选中节点配置表
class BmcCheckoutConf(models.Model):
    # uuid = models.AutoField(primary_key=True,verbose_name='自增主键')
    nodeid = models.ForeignKey(NodeInfo,verbose_name='节点表外键',on_delete=models.CASCADE)
    bmcConfId = models.ForeignKey(BmcConfName,verbose_name='BMC配制表外键',on_delete=models.CASCADE)

    class Meta:
        verbose_name = verbose_name_plural = 'BMC选中节点配置表'

#BMC配置信息(用于填写所有节点的配置信息,如果多个节点的BMC信息不相同取并集，取不到的值为空)
class BmcConfig(models.Model):
    uuid = models.AutoField(primary_key=True,verbose_name='自增主键')
    confId = models.ForeignKey(BmcConfName,verbose_name='配置名称表UUID',on_delete=models.CASCADE)
    keyword = models.CharField(max_length=128,verbose_name='关键字')
    description = models.CharField(max_length=128,verbose_name='关键字描述')
    remark = models.CharField(max_length=128,verbose_name='备注')

    class Meta:
        verbose_name = verbose_name_plural = 'BMC配置表'

