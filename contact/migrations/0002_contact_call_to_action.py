# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):
    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='call_to_action',
            field=djangocms_text_ckeditor.fields.HTMLField(default=''),
            preserve_default=False,
        ),
    ]
