# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-09 22:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('widgets', '0015_auto_20171109_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='widget',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='winner', to='widgets.Leed'),
        ),
    ]