# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Attachment'
        db.create_table('banzai_attachment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('package', self.gf('django.db.models.fields.related.ForeignKey')(related_name='attachments', to=orm['banzai.Package'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('banzai', ['Attachment'])


    def backwards(self, orm):
        # Deleting model 'Attachment'
        db.delete_table('banzai_attachment')


    models = {
        'banzai.attachment': {
            'Meta': {'object_name': 'Attachment'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'package': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'attachments'", 'to': "orm['banzai.Package']"})
        },
        'banzai.package': {
            'Meta': {'object_name': 'Package'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'emails_all': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'emails_correct': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pack_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'})
        },
        'banzai.report': {
            'Meta': {'object_name': 'Report'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'package': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports'", 'to': "orm['banzai.Package']"}),
            'reject_code': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'reject_message': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'})
        },
        'banzai.reportfbl': {
            'Meta': {'object_name': 'ReportFBL'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'package': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reports_fbl'", 'to': "orm['banzai.Package']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'})
        }
    }

    complete_apps = ['banzai']