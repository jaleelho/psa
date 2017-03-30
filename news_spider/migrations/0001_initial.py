# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-04 05:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='\u9891\u9053\u540d\u79f0')),
                ('link', models.URLField(unique=True, verbose_name='\u9891\u9053\u94fe\u63a5')),
            ],
            options={
                'verbose_name': '\u65b0\u95fb\u9891\u9053',
                'verbose_name_plural': '\u65b0\u95fb\u9891\u9053',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_id', models.CharField(max_length=20, verbose_name='\u65b0\u95fbID')),
                ('title', models.CharField(max_length=256, verbose_name='\u65b0\u95fb\u6807\u9898')),
                ('doc_url', models.URLField(verbose_name='\u65b0\u95fb\u6b63\u6587\u94fe\u63a5')),
                ('img_url', models.URLField(verbose_name='\u65b0\u95fb\u56fe\u7247\u94fe\u63a5')),
                ('comment_count', models.IntegerField(default=0, verbose_name='\u8bc4\u8bba\u6570')),
                ('label', models.CharField(blank=True, max_length=256, null=True, verbose_name='\u6807\u7b7e')),
                ('keywords', models.CharField(blank=True, max_length=256, null=True, verbose_name='\u5173\u952e\u5b57')),
                ('publish_at', models.DateTimeField(verbose_name='\u65b0\u95fb\u53d1\u5e03\u65f6\u95f4')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_spider.Channel', verbose_name='\u6240\u5c5e\u9891\u9053')),
            ],
            options={
                'verbose_name': '\u65b0\u95fb\u6761\u76ee',
                'verbose_name_plural': '\u65b0\u95fb\u6761\u76ee',
            },
        ),
    ]
