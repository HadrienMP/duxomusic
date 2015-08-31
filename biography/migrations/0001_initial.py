# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0011_auto_20150419_1006'),
        ('filer', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biography',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('description', djangocms_text_ckeditor.fields.HTMLField()),
                ('hover_photo', filer.fields.image.FilerImageField(related_name='hover_photo', blank=True, to='filer.Image', null=True)),
                ('photo', filer.fields.image.FilerImageField(related_name='photo', to='filer.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
