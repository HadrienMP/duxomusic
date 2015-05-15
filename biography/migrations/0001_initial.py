# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):
    dependencies = [
        ('filer', '0002_auto_20150510_1856'),
        ('cms', '0011_auto_20150419_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biography',
            fields=[
                ('cmsplugin_ptr',
                 models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False,
                                      to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=125)),
                ('biography', djangocms_text_ckeditor.fields.HTMLField()),
                ('photo', filer.fields.image.FilerImageField(to='filer.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
