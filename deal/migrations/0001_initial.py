# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Deal'
        db.create_table(u'deal_deal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('short_desc', self.gf('django.db.models.fields.CharField')(default='No Description', max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=1000)),
            ('cost_per_unit', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('num_units', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('category', self.gf('django.db.models.fields.CharField')(default='OTHR', max_length=4)),
            ('delivery_method', self.gf('django.db.models.fields.TextField')()),
            ('min_pledge_amount', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('time_posted', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('last_modified_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'deal', ['Deal'])

        # Adding M2M table for field search_tags on 'Deal'
        m2m_table_name = db.shorten_name(u'deal_deal_search_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('deal', models.ForeignKey(orm[u'deal.deal'], null=False)),
            ('searchtag', models.ForeignKey(orm[u'deal.searchtag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['deal_id', 'searchtag_id'])

        # Adding model 'SearchTag'
        db.create_table(u'deal_searchtag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
        ))
        db.send_create_signal(u'deal', ['SearchTag'])


    def backwards(self, orm):
        # Deleting model 'Deal'
        db.delete_table(u'deal_deal')

        # Removing M2M table for field search_tags on 'Deal'
        db.delete_table(db.shorten_name(u'deal_deal_search_tags'))

        # Deleting model 'SearchTag'
        db.delete_table(u'deal_searchtag')


    models = {
        u'deal.deal': {
            'Meta': {'object_name': 'Deal'},
            'category': ('django.db.models.fields.CharField', [], {'default': "'OTHR'", 'max_length': '4'}),
            'cost_per_unit': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'delivery_method': ('django.db.models.fields.TextField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'min_pledge_amount': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'num_units': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'search_tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['deal.SearchTag']", 'symmetrical': 'False'}),
            'short_desc': ('django.db.models.fields.CharField', [], {'default': "'No Description'", 'max_length': '200'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'time_posted': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'deal.searchtag': {
            'Meta': {'object_name': 'SearchTag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        }
    }

    complete_apps = ['deal']