# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2020-03-01 04:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200301_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 1, 4, 40, 48, 885694, tzinfo=utc)),
        ),
    ]
