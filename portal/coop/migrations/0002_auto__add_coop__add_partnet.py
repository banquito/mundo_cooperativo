# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Coop'
        db.create_table(u'coop_coop', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'coop', ['Coop'])

        # Adding model 'Partnet'
        db.create_table(u'coop_partnet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('coop', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coop.Coop'])),
        ))
        db.send_create_signal(u'coop', ['Partnet'])


    def backwards(self, orm):
        # Deleting model 'Coop'
        db.delete_table(u'coop_coop')

        # Deleting model 'Partnet'
        db.delete_table(u'coop_partnet')


    models = {
        u'coop.coop': {
            'Meta': {'object_name': 'Coop'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'coop.partnet': {
            'Meta': {'object_name': 'Partnet'},
            'coop': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['coop.Coop']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['coop']