# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):
    dependencies = [
        ('biography', '0007_biography_hover_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biography',
            name='hover_photo',
            field=filer.fields.image.FilerImageField(related_name='hover_photo', blank=True, to='filer.Image',
                                                     null=True),
            preserve_default=True,
        ),
    ]
