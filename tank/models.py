from django.db import models

#CDU连接配置表
class CduConfig(models.Model):

    connChoice = [
        (1,'RS485'),
        (2,'MODBUS TCP')
    ]
    pCheck = [
        ('N','不校验'),
        ('O','奇校验'),
        ('E','偶校验'),
    ]
    uuid = models.AutoField(primary_key=True,verbose_name='CDU连接配置表主键')
    connWay = models.IntegerField(choices = connChoice,verbose_name='连接方式')
    devPath = models.CharField(max_length=128,verbose_name='设备路径',blank=True,null=True)
    ipAddr = models.CharField(max_length=128,verbose_name='IP地址',blank=True,null=True)
    port = models.IntegerField(verbose_name='端口号',blank=True,null=True)
    parityCheck = models.CharField(max_length=128,choices=pCheck,verbose_name='校验方式')


    class Meta:
        verbose_name = verbose_name_plural = 'CDU连接配置表'

