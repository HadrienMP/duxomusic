# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models, migrations
import uuidfield.fields


class Migration(migrations.Migration):
    dependencies = [
        ('cms', '0011_auto_20150419_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(unique=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_modification', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sujet', models.CharField(unique=True, max_length=255)),
                ('corps', models.TextField()),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_modification', models.DateTimeField(auto_now=True)),
                ('date_envoi', models.DateTimeField(default=datetime.datetime.now)),
                ('draft', models.BooleanField(default=True)),
                ('sent', models.BooleanField(default=False)),
                ('list', models.ForeignKey(related_name='mails', to='newsletter.List')),
            ],
            options={
                'ordering': ['-date_envoi'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NewsletterPluginModel',
            fields=[
                ('cmsplugin_ptr',
                 models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False,
                                      to='cms.CMSPlugin')),
                ('call_to_action', models.TextField(null=True, verbose_name=b'Call To Action', blank=True)),
                ('list', models.ForeignKey(to='newsletter.List')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('prenom', models.CharField(max_length=255)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_modification', models.DateTimeField(auto_now=True)),
                ('date_desinscription', models.DateTimeField(null=True, blank=True)),
                ('opt_in', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
                ('token', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, blank=True)),
            ],
            options={
                'verbose_name': 'personne',
                'verbose_name_plural': 'personnes',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='mail',
            name='readers',
            field=models.ManyToManyField(related_name='read_mails', to='newsletter.Person', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mail',
            name='recipients',
            field=models.ManyToManyField(to='newsletter.Person', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='list',
            name='subscribers',
            field=models.ManyToManyField(related_name='lists', to='newsletter.Person', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='link',
            name='clickers',
            field=models.ManyToManyField(to='newsletter.Person', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='link',
            name='mail',
            field=models.ForeignKey(related_name='links', to='newsletter.Mail'),
            preserve_default=True,
        ),
    ]
