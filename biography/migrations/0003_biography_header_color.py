# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorfield.fields


class Migration(migrations.Migration):
    dependencies = [
        ('biography', '0002_auto_20150515_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='biography',
            name='header_color',
            field=colorfield.fields.ColorField(default=b'444444', max_length=7),
            preserve_default=True,
        ),
    ]
