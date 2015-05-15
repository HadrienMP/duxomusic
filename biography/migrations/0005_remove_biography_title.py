# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('biography', '0004_auto_20150515_1028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biography',
            name='title',
        ),
    ]
