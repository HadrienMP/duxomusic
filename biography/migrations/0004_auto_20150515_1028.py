# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorfield.fields


class Migration(migrations.Migration):
    dependencies = [
        ('biography', '0003_biography_header_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biography',
            name='header_color',
            field=colorfield.fields.ColorField(max_length=7, blank=True),
            preserve_default=True,
        ),
    ]
