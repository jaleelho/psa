# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-08 10:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news_analyzer', '0002_auto_20170108_1709'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='analysistask',
            options={'verbose_name': '\u65b0\u95fb\u5206\u6790\u4efb\u52a1', 'verbose_name_plural': '\u65b0\u95fb\u5206\u6790\u4efb\u52a1'},
        ),
        migrations.AddField(
            model_name='analysistask',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='\u4efb\u52a1\u521b\u5efa\u65f6\u95f4'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='analysistask',
            name='start_time',
            field=models.DateTimeField(null=True, verbose_name='\u5206\u6790\u5f00\u59cb\u65f6\u95f4'),
        ),
    ]
