# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit_autosuggest.managers


class Migration(migrations.Migration):
    dependencies = [
        ('dux_news', '0004_sound_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sound',
            name='tags',
            field=taggit_autosuggest.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True,
                                                              help_text='A comma-separated list of tags.',
                                                              verbose_name='Tags'),
            preserve_default=True,
        ),
    ]
