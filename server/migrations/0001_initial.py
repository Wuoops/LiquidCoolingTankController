# Generated by Django 2.1.8 on 2020-03-22 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NodeInfo',
            fields=[
                ('uuid', models.AutoField(primary_key=True, serialize=False, verbose_name='自增主键')),
                ('nodeName', models.CharField(max_length=128, verbose_name='节点名称')),
                ('nodeIP', models.CharField(max_length=128, verbose_name='节点IP地址')),
                ('nodeMac', models.CharField(max_length=128, verbose_name='节点MAC地址')),
                ('bmcUserName', models.CharField(max_length=128, verbose_name='BMC帐号')),
                ('bmcPassword', models.CharField(max_length=128, verbose_name='BMC密码')),
                ('nodeStatus', models.IntegerField(verbose_name='节点运行状态码(0：关机，1：运行中，2：标记运行,3：标记关机,4：其他标记)')),
                ('remark', models.TextField(help_text='备注信息', verbose_name='备注')),
            ],
            options={
                'verbose_name': 'SERVER信息表',
                'verbose_name_plural': 'SERVER信息表',
            },
        ),
    ]