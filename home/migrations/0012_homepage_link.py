# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_homepage_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='link',
            field=models.URLField(blank=True),
        ),
    ]
