# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CServices', '0002_wipreq_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='wipreq',
            name='method',
            field=models.CharField(max_length=20, null=True, choices=[('phone', 'phone'), ('online', 'online'), ('qual recruit', 'qual recruit'), ('room rental', 'room rental')]),
        ),
    ]
