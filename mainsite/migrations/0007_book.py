# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-16 12:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0006_auto_20170716_1139'),
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pages', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('authors', models.ManyToManyField(to='mainsite.author')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.publisher')),
                ('tags', models.ManyToManyField(to='mainsite.subject')),
            ],
        ),
    ]
