# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):
    dependencies = [
        ('biography', '0005_remove_biography_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biography',
            name='header_color',
        ),
        migrations.AlterField(
            model_name='biography',
            name='photo',
            field=filer.fields.image.FilerImageField(related_name='photo', to='filer.Image'),
            preserve_default=True,
        ),
    ]
