# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-03 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drawing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='page_kind',
            field=models.CharField(default=1, max_length=15, verbose_name='\u30da\u30fc\u30b8\u5206\u985e'),
            preserve_default=False,
        ),
    ]
