# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('duxomusic', '0001_squashed_0003_auto_20150912_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='background',
            name='color',
            field=colorfield.fields.ColorField(default=b'000000', max_length=7, verbose_name=b'Couleur de fond'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='background',
            name='no_background_split',
            field=models.IntegerField(default=480, verbose_name=b"Taille \xc3\xa0 partir de laquelle on n'affiche plus l'image de fond"),
            preserve_default=True,
        ),
    ]
