# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 16:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('color_library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='color',
            name='category',
        ),
        migrations.RemoveField(
            model_name='color',
            name='sub_category',
        ),
    ]