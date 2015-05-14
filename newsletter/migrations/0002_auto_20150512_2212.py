# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models, migrations
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='date_envoi',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 12, 20, 12, 12, 81847, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
