# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2020-02-29 07:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200229_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 29, 7, 57, 7, 804642, tzinfo=utc)),
        ),
    ]
