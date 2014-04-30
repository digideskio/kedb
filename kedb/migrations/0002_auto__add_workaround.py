# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Workaround'
        db.create_table('kedb_workaround', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('known_error', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['kedb.KnownError'])),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('temporary', self.gf('django.db.models.fields.BooleanField')(default=False, max_length=255)),
        ))
        db.send_create_signal('kedb', ['Workaround'])


    def backwards(self, orm):
        # Deleting model 'Workaround'
        db.delete_table('kedb_workaround')


    models = {
        'kedb.knownerror': {
            'Meta': {'object_name': 'KnownError'},
            'check': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'default': "'level1'", 'max_length': '55'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'output_pattern': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'severity': ('django.db.models.fields.CharField', [], {'default': "'medium'", 'max_length': '55'})
        },
        'kedb.workaround': {
            'Meta': {'object_name': 'Workaround'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'known_error': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['kedb.KnownError']"}),
            'temporary': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'max_length': '255'})
        }
    }

    complete_apps = ['kedb']