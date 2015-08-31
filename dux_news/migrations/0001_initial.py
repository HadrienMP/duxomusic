# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import taggit_autosuggest.managers
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        ('cms', '0011_auto_20150419_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewSound',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Sound',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sound', models.TextField(max_length=500)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_modification', models.DateTimeField(auto_now=True)),
                ('date_publication', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_depublication', models.DateTimeField(null=True, blank=True)),
                ('draft', models.BooleanField(default=True)),
                ('description', djangocms_text_ckeditor.fields.HTMLField(blank=True)),
                ('title', models.CharField(max_length=125)),
                ('slug', models.SlugField(unique=True)),
                ('tags', taggit_autosuggest.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='newsound',
            name='sound',
            field=models.ForeignKey(to='dux_news.Sound'),
            preserve_default=True,
        ),
    ]
