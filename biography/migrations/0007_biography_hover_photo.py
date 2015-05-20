# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):
    dependencies = [
        ('filer', '0002_auto_20150510_1856'),
        ('biography', '0006_auto_20150519_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='biography',
            name='hover_photo',
            field=filer.fields.image.FilerImageField(related_name='hover_photo', default=1, to='filer.Image'),
            preserve_default=False,
        ),
    ]
