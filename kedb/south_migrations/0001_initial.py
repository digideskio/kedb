# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'KnownError'
        db.create_table('kedb_knownerror', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('check', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('output_pattern', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('level', self.gf('django.db.models.fields.CharField')(default='L1', max_length=55)),
            ('severity', self.gf('django.db.models.fields.CharField')(default='medium', max_length=55)),
        ))
        db.send_create_signal('kedb', ['KnownError'])


    def backwards(self, orm):
        # Deleting model 'KnownError'
        db.delete_table('kedb_knownerror')


    models = {
        'kedb.knownerror': {
            'Meta': {'object_name': 'KnownError'},
            'check': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'default': "'L1'", 'max_length': '55'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'output_pattern': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'severity': ('django.db.models.fields.CharField', [], {'default': "'medium'", 'max_length': '55'})
        }
    }

    complete_apps = ['kedb']