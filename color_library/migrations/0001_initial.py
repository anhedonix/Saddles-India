# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 10:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('published_date', models.DateTimeField(blank=True, editable=False, null=True)),
                ('col_l', models.FloatField(verbose_name='L')),
                ('col_a', models.FloatField(verbose_name=' a')),
                ('col_b', models.FloatField(verbose_name=' b')),
                ('col_c', models.FloatField(verbose_name='C')),
                ('col_h', models.FloatField(verbose_name=' h')),
                ('R', models.FloatField(editable=False)),
                ('G', models.FloatField(editable=False)),
                ('B', models.FloatField(editable=False)),
                ('H', models.FloatField(blank=True, editable=False, null=True)),
                ('S', models.FloatField(blank=True, editable=False, null=True)),
                ('V', models.FloatField(blank=True, editable=False, null=True)),
                ('Hex', models.CharField(editable=False, max_length=6)),
                ('author', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='color_library.Category', verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Main Category')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='main_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='color_library.MainCategory', verbose_name='Main Category'),
        ),
    ]
