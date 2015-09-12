# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('duxomusic', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='background',
            name='images',
        ),
        migrations.AddField(
            model_name='imagewrapper',
            name='background',
            field=models.ForeignKey(default=0, to='duxomusic.Background'),
            preserve_default=False,
        ),
    ]
