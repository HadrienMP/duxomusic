# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('duxomusic', '0002_auto_20150912_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagewrapper',
            name='background',
            field=models.ForeignKey(related_name='images', to='duxomusic.Background'),
            preserve_default=True,
        ),
    ]
