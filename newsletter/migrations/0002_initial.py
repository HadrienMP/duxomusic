# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table(u'newsletter_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('date_creation', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modification', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_descinscription', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'newsletter', ['Person'])

        # Adding model 'Mail'
        db.create_table(u'newsletter_mail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sujet', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('corps', self.gf('django.db.models.fields.TextField')()),
            ('date_creation', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modification', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'newsletter', ['Mail'])

        # Adding M2M table for field recipients on 'Mail'
        m2m_table_name = db.shorten_name(u'newsletter_mail_recipients')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mail', models.ForeignKey(orm[u'newsletter.mail'], null=False)),
            ('person', models.ForeignKey(orm[u'newsletter.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['mail_id', 'person_id'])

        # Adding M2M table for field readers on 'Mail'
        m2m_table_name = db.shorten_name(u'newsletter_mail_readers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mail', models.ForeignKey(orm[u'newsletter.mail'], null=False)),
            ('person', models.ForeignKey(orm[u'newsletter.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['mail_id', 'person_id'])

        # Adding model 'List'
        db.create_table(u'newsletter_list', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('date_creation', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modification', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'newsletter', ['List'])

        # Adding M2M table for field mails on 'List'
        m2m_table_name = db.shorten_name(u'newsletter_list_mails')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('list', models.ForeignKey(orm[u'newsletter.list'], null=False)),
            ('mail', models.ForeignKey(orm[u'newsletter.mail'], null=False))
        ))
        db.create_unique(m2m_table_name, ['list_id', 'mail_id'])

        # Adding M2M table for field subscribers on 'List'
        m2m_table_name = db.shorten_name(u'newsletter_list_subscribers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('list', models.ForeignKey(orm[u'newsletter.list'], null=False)),
            ('person', models.ForeignKey(orm[u'newsletter.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['list_id', 'person_id'])

        # Adding model 'Link'
        db.create_table(u'newsletter_link', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('mail', self.gf('django.db.models.fields.related.ForeignKey')(related_name='links', to=orm['newsletter.Mail'])),
        ))
        db.send_create_signal(u'newsletter', ['Link'])

        # Adding M2M table for field clickers on 'Link'
        m2m_table_name = db.shorten_name(u'newsletter_link_clickers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('link', models.ForeignKey(orm[u'newsletter.link'], null=False)),
            ('person', models.ForeignKey(orm[u'newsletter.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['link_id', 'person_id'])

        # Adding model 'NewsletterPluginModel'
        db.create_table(u'newsletter_newsletterpluginmodel', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('list', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['newsletter.List'])),
        ))
        db.send_create_signal(u'newsletter', ['NewsletterPluginModel'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table(u'newsletter_person')

        # Deleting model 'Mail'
        db.delete_table(u'newsletter_mail')

        # Removing M2M table for field recipients on 'Mail'
        db.delete_table(db.shorten_name(u'newsletter_mail_recipients'))

        # Removing M2M table for field readers on 'Mail'
        db.delete_table(db.shorten_name(u'newsletter_mail_readers'))

        # Deleting model 'List'
        db.delete_table(u'newsletter_list')

        # Removing M2M table for field mails on 'List'
        db.delete_table(db.shorten_name(u'newsletter_list_mails'))

        # Removing M2M table for field subscribers on 'List'
        db.delete_table(db.shorten_name(u'newsletter_list_subscribers'))

        # Deleting model 'Link'
        db.delete_table(u'newsletter_link')

        # Removing M2M table for field clickers on 'Link'
        db.delete_table(db.shorten_name(u'newsletter_link_clickers'))

        # Deleting model 'NewsletterPluginModel'
        db.delete_table(u'newsletter_newsletterpluginmodel')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        u'newsletter.link': {
            'Meta': {'object_name': 'Link'},
            'clickers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['newsletter.Person']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mail': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'links'", 'to': u"orm['newsletter.Mail']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'newsletter.list': {
            'Meta': {'object_name': 'List'},
            'date_creation': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modification': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mails': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['newsletter.Mail']", 'symmetrical': 'False', 'blank': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'subscribers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['newsletter.Person']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'newsletter.mail': {
            'Meta': {'object_name': 'Mail'},
            'corps': ('django.db.models.fields.TextField', [], {}),
            'date_creation': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modification': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'readers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'read_mails'", 'blank': 'True', 'to': u"orm['newsletter.Person']"}),
            'recipients': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'received_mails'", 'blank': 'True', 'to': u"orm['newsletter.Person']"}),
            'sujet': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'newsletter.newsletterpluginmodel': {
            'Meta': {'object_name': 'NewsletterPluginModel', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'list': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['newsletter.List']"})
        },
        u'newsletter.person': {
            'Meta': {'object_name': 'Person'},
            'date_creation': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_descinscription': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_modification': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['newsletter']