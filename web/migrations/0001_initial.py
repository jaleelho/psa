# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-30 13:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('news_spider', '0006_newscomment_province'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='\u7535\u5b50\u90ae\u7bb1')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65e5\u671f')),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribe_emails', to='news_spider.Channel', verbose_name='\u8ba2\u9605\u9891\u9053')),
            ],
            options={
                'verbose_name': '\u65b0\u95fb\u9891\u9053',
                'verbose_name_plural': '\u65b0\u95fb\u9891\u9053',
            },
        ),
    ]
