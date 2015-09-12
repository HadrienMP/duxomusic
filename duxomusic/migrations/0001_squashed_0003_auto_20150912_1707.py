# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):

    replaces = [(b'duxomusic', '0001_initial'), (b'duxomusic', '0002_auto_20150912_1703'), (b'duxomusic', '0003_auto_20150912_1707')]

    dependencies = [
        ('filer', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Background',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=False, verbose_name=b'Actif')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ImageWrapper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', filer.fields.image.FilerImageField(to=b'filer.Image')),
                ('background', models.ForeignKey(related_name='images', to='duxomusic.Background')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
