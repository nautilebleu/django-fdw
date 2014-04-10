# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Album'
        db.create_table(u'catalog_album', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('publish_year', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'catalog', ['Album'])

        # Adding model 'Song'
        db.create_table(u'catalog_song', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(related_name='songs', to=orm['catalog.Album'])),
        ))
        db.send_create_signal(u'catalog', ['Song'])


    def backwards(self, orm):
        # Deleting model 'Album'
        db.delete_table(u'catalog_album')

        # Deleting model 'Song'
        db.delete_table(u'catalog_song')


    models = {
        u'catalog.album': {
            'Meta': {'object_name': 'Album'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publish_year': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'catalog.song': {
            'Meta': {'object_name': 'Song'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'songs'", 'to': u"orm['catalog.Album']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['catalog']