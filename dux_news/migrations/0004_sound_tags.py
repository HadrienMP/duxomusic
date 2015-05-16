# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit_autosuggest.managers


class Migration(migrations.Migration):
    dependencies = [
        ('taggit', '0001_initial'),
        ('dux_news', '0003_auto_20150514_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='sound',
            name='tags',
            field=taggit_autosuggest.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem',
                                                              help_text='A comma-separated list of tags.',
                                                              verbose_name='Tags'),
            preserve_default=True,
        ),
    ]
