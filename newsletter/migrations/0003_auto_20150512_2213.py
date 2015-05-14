# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ('newsletter', '0002_auto_20150512_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='date_envoi',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
    ]
