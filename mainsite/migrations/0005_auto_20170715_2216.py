# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-15 22:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0004_auto_20170715_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.DecimalField(decimal_places=0, max_digits=9),
        ),
    ]
