# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-07-29 15:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0004_auto_20180729_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='shipments', to='shipments.Company'),
        ),
    ]
