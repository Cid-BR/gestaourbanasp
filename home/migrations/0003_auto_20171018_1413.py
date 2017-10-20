# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-18 16:13
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_staticpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticpage',
            name='corpo',
            field=wagtail.wagtailcore.fields.StreamField((('Parágrafo', wagtail.wagtailcore.blocks.RichTextBlock()), ('Imagem', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('HTML', wagtail.wagtailcore.blocks.RawHTMLBlock()))),
        ),
    ]