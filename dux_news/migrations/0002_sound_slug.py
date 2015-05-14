# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('dux_news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sound',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
