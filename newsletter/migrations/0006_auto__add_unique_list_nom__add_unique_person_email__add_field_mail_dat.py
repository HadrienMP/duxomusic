# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field mails on 'List'
        db.delete_table(db.shorten_name(u'newsletter_list_mails'))

        # Adding unique constraint on 'List', fields ['nom']
        db.create_unique(u'newsletter_list', ['nom'])

        # Adding unique constraint on 'Person', fields ['email']
        db.create_unique(u'newsletter_person', ['email'])

        # Adding field 'Mail.date_envoi'
        db.add_column(u'newsletter_mail', 'date_envoi',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 4, 3, 0, 0)),
                      keep_default=False)

        # Adding field 'Mail.draft'
        db.add_column(u'newsletter_mail', 'draft',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Mail.list'
        db.add_column(u'newsletter_mail', 'list',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='mails', to=orm['newsletter.List']),
                      keep_default=False)

        # Adding unique constraint on 'Mail', fields ['sujet']
        db.create_unique(u'newsletter_mail', ['sujet'])


    def backwards(self, orm):
        # Removing unique constraint on 'Mail', fields ['sujet']
        db.delete_unique(u'newsletter_mail', ['sujet'])

        # Removing unique constraint on 'Person', fields ['email']
        db.delete_unique(u'newsletter_person', ['email'])

        # Removing unique constraint on 'List', fields ['nom']
        db.delete_unique(u'newsletter_list', ['nom'])

        # Adding M2M table for field mails on 'List'
        m2m_table_name = db.shorten_name(u'newsletter_list_mails')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('list', models.ForeignKey(orm[u'newsletter.list'], null=False)),
            ('mail', models.ForeignKey(orm[u'newsletter.mail'], null=False))
        ))
        db.create_unique(m2m_table_name, ['list_id', 'mail_id'])

        # Deleting field 'Mail.date_envoi'
        db.delete_column(u'newsletter_mail', 'date_envoi')

        # Deleting field 'Mail.draft'
        db.delete_column(u'newsletter_mail', 'draft')

        # Deleting field 'Mail.list'
        db.delete_column(u'newsletter_mail', 'list_id')


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
            'nom': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'subscribers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['newsletter.Person']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'newsletter.mail': {
            'Meta': {'object_name': 'Mail'},
            'corps': ('django.db.models.fields.TextField', [], {}),
            'date_creation': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_envoi': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 4, 3, 0, 0)'}),
            'date_modification': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'draft': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mails'", 'to': u"orm['newsletter.List']"}),
            'readers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'read_mails'", 'blank': 'True', 'to': u"orm['newsletter.Person']"}),
            'recipients': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'received_mails'", 'blank': 'True', 'to': u"orm['newsletter.Person']"}),
            'sujet': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'newsletter.newsletterpluginmodel': {
            'Meta': {'object_name': 'NewsletterPluginModel', '_ormbases': ['cms.CMSPlugin']},
            'call_to_action': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'list': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['newsletter.List']"})
        },
        u'newsletter.person': {
            'Meta': {'object_name': 'Person'},
            'date_creation': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_desinscription': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_modification': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['newsletter']