# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 19:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('titulo', models.CharField(blank=True, default='Título', help_text='O título do evento.', max_length=140)),
                ('endereco', models.CharField(max_length=255)),
                ('data_inicio', models.DateField(verbose_name='Data de Início')),
                ('data_final', models.DateField(verbose_name='Data Final')),
                ('horario_inicio', models.TimeField(verbose_name='Horário de Início')),
                ('horario_final', models.TimeField(verbose_name='Horário Final')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventsIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='events',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='events.EventsIndexPage'),
        ),
    ]