# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import colorfield.fields
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150510_1856'),
        ('cms', '0011_auto_20150419_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('cmsplugin_ptr',
                 models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False,
                                      to='cms.CMSPlugin')),
                ('call_to_action', djangocms_text_ckeditor.fields.HTMLField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='ContactItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(null=True, verbose_name=b'URL', blank=True)),
                ('mail', models.EmailField(max_length=254, null=True, verbose_name=b'Email', blank=True)),
                ('title', models.CharField(default=b'Contact',
                                           help_text=b"Affich\xc3\xa9 au survol de l'image repr\xc3\xa9sentant le contact",
                                           max_length=50, verbose_name=b'Titre')),
                ('fa', models.CharField(help_text=b"Ajoutez ici le nom d'une ic\xc3\xb4ne Font-Awesome", max_length=50,
                                        null=True, verbose_name=b'Icone Font Awesome', blank=True)),
                ('bgcolor', colorfield.fields.ColorField(default=b'444444', max_length=7, null=True,
                                                         verbose_name=b'Couleur de fond', blank=True)),
                ('icon', filer.fields.image.FilerImageField(related_name='contact_icon', blank=True, to='filer.Image',
                                                            help_text=b"Modifi\xc3\xa9e automatiquement pour atteindre une taille de 100px x 100px. Si vous ne remplissez pas ce champ l'application tentera d'afficher l'icone Font-Awesome.",
                                                            null=True)),
                ('plugin', models.ForeignKey(related_name='items', to='contact.Contact')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
