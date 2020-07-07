from django.db import models

#设备路径关系表
class sensorModelConfig(models.Model):

    uuid = models.AutoField(primary_key=True,verbose_name='自增主键')
    devName = models.CharField(max_length=128 ,verbose_name='设备路径')
    modelName = models.CharField(max_length=128,verbose_name='设备名称')
    remark = models.TextField(verbose_name='描述',help_text='详细描述一下该设备的作用')

    class Meta:
        verbose_name = verbose_name_plural = '设备路径关系表'
#传感器配置名词关系对照表
class sensorConfigName(models.Model):

    uuid = models.AutoField(primary_key=True,verbose_name='自增主键')
    configName = models.CharField(max_length=1000,verbose_name='配置名称')
    remark = models.TextField(verbose_name='描述',help_text='详细描述一下该配置')

    class Meta:
        verbose_name = verbose_name_plural = '传感器配置名称关系对照表'

#传感器位置关系表
class sensorConfig(models.Model):

    uuid = models.AutoField(primary_key=True,verbose_name='自增主键')
    # modelPk = models.ForeignKey(sensorModelConfig,verbose_name='设备', on_delete=models.CASCADE)
    sensorConf = models.ForeignKey(sensorConfigName,verbose_name='配置',on_delete=models.CASCADE)
    sensorId = models.IntegerField(verbose_name='传感器编号')
    sensorName = models.CharField(max_length=500,verbose_name='传感器名词/位置')
    remark = models.TextField(verbose_name='描述',help_text='详细描述一下该传感器的位置和作用')

    class Meta:
        verbose_name = verbose_name_plural = '传感器位置关系表'
#选中的配置表
class sensorCheckout(models.Model):

    modelUUID = models.ForeignKey(sensorModelConfig,verbose_name='选中的设备表UUID',on_delete=models.CASCADE)
    configUUID = models.ForeignKey(sensorConfigName,verbose_name='选中的配置表UUID',on_delete=models.CASCADE)
    numOfCheckedModels = models.IntegerField(default=1,verbose_name='生效的模块数量')
    class Meta:
        verbose_name = verbose_name_plural = '选中的配置'
