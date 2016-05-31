# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CServices', '0003_wipreq_method'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wipreq',
            old_name='method',
            new_name='meth',
        ),
    ]
