# Generated by Django 2.1.8 on 2020-04-07 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CduConfig',
            fields=[
                ('uuid', models.AutoField(primary_key=True, serialize=False, verbose_name='CDU连接配置表主键')),
                ('connWay', models.IntegerField(choices=[(1, 'RS485'), (2, 'MODBUS TCP')], verbose_name='连接方式')),
                ('devPath', models.CharField(blank=True, max_length=128, null=True, verbose_name='设备路径')),
                ('ipAddr', models.CharField(blank=True, max_length=128, null=True, verbose_name='IP地址')),
                ('port', models.IntegerField(blank=True, null=True, verbose_name='端口号')),
                ('parityCheck', models.CharField(choices=[('N', '不校验'), ('O', '奇校验'), ('E', '偶校验')], max_length=128, verbose_name='校验方式')),
            ],
            options={
                'verbose_name': 'CDU连接配置表',
                'verbose_name_plural': 'CDU连接配置表',
            },
        ),
    ]