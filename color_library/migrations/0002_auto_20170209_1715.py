# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 11:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('color_library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Tag')),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='main_category',
        ),
        migrations.AddField(
            model_name='color',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='category',
            field=models.ForeignKey(help_text='What category does this leather come under? Ex: Napa, Exports.', on_delete=django.db.models.deletion.CASCADE, to='color_library.Category', verbose_name='Category'),
        ),
        migrations.DeleteModel(
            name='MainCategory',
        ),
        migrations.AddField(
            model_name='color',
            name='tags',
            field=models.ManyToManyField(help_text='What can this leather be described as? Ex: Tan, Beige, Black, Mud.', to='color_library.Tag', verbose_name='Tags'),
        ),
    ]
