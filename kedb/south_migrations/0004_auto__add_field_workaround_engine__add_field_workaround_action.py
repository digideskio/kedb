# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Workaround.engine'
        db.add_column('kedb_workaround', 'engine',
                      self.gf('django.db.models.fields.CharField')(default='salt', max_length=255),
                      keep_default=False)

        # Adding field 'Workaround.action'
        db.add_column('kedb_workaround', 'action',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Workaround.engine'
        db.delete_column('kedb_workaround', 'engine')

        # Deleting field 'Workaround.action'
        db.delete_column('kedb_workaround', 'action')


    models = {
        'kedb.knownerror': {
            'Meta': {'object_name': 'KnownError'},
            'check': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'default': "'level1'", 'max_length': '55'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'output_pattern': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ownership': ('django.db.models.fields.CharField', [], {'default': "'cloudlab'", 'max_length': '55'}),
            'severity': ('django.db.models.fields.CharField', [], {'default': "'medium'", 'max_length': '55'})
        },
        'kedb.workaround': {
            'Meta': {'object_name': 'Workaround'},
            'action': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'engine': ('django.db.models.fields.CharField', [], {'default': "'salt'", 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'known_error': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'workarounds'", 'to': "orm['kedb.KnownError']"}),
            'temporary': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'max_length': '255'})
        }
    }

    complete_apps = ['kedb']