# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('dux_news', '0002_sound_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sound',
            name='slug',
            field=models.SlugField(unique=True),
            preserve_default=True,
        ),
    ]
