# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 13:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('home', '0004_auto_20170922_1013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='headings',
        ),
        migrations.AddField(
            model_name='homepage',
            name='heading',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='homepage',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
