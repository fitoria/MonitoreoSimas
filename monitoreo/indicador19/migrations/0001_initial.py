# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Causa'
        db.create_table('indicador19_causa', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('indicador19', ['Causa'])

        # Adding model 'Fenomeno'
        db.create_table('indicador19_fenomeno', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('causa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indicador19.Causa'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('indicador19', ['Fenomeno'])

        # Adding model 'Graves'
        db.create_table('indicador19_graves', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('indicador19', ['Graves'])

        # Adding model 'Vulnerable'
        db.create_table('indicador19_vulnerable', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('motivo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indicador19.Fenomeno'])),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simas.Encuesta'])),
        ))
        db.send_create_signal('indicador19', ['Vulnerable'])

        # Adding M2M table for field respuesta on 'Vulnerable'
        db.create_table('indicador19_vulnerable_respuesta', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('vulnerable', models.ForeignKey(orm['indicador19.vulnerable'], null=False)),
            ('graves', models.ForeignKey(orm['indicador19.graves'], null=False))
        ))
        db.create_unique('indicador19_vulnerable_respuesta', ['vulnerable_id', 'graves_id'])


    def backwards(self, orm):
        
        # Deleting model 'Causa'
        db.delete_table('indicador19_causa')

        # Deleting model 'Fenomeno'
        db.delete_table('indicador19_fenomeno')

        # Deleting model 'Graves'
        db.delete_table('indicador19_graves')

        # Deleting model 'Vulnerable'
        db.delete_table('indicador19_vulnerable')

        # Removing M2M table for field respuesta on 'Vulnerable'
        db.delete_table('indicador19_vulnerable_respuesta')


    models = {
        'indicador19.causa': {
            'Meta': {'object_name': 'Causa'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'indicador19.fenomeno': {
            'Meta': {'object_name': 'Fenomeno'},
            'causa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indicador19.Causa']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'indicador19.graves': {
            'Meta': {'object_name': 'Graves'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'indicador19.vulnerable': {
            'Meta': {'object_name': 'Vulnerable'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['simas.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'motivo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indicador19.Fenomeno']"}),
            'respuesta': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['indicador19.Graves']", 'symmetrical': 'False'})
        },
        'lugar.comunidad': {
            'Meta': {'object_name': 'Comunidad'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'lugar.departamento': {
            'Meta': {'object_name': 'Departamento'},
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'db_index': 'True'})
        },
        'lugar.municipio': {
            'Meta': {'ordering': "['departamento__nombre']", 'object_name': 'Municipio'},
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Departamento']"}),
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'db_index': 'True'})
        },
        'simas.encuesta': {
            'Meta': {'object_name': 'Encuesta'},
            'cedula': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'comunidad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Comunidad']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'finca': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'organizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['simas.Organizaciones']"}),
            'recolector': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['simas.Recolector']"}),
            'sexo': ('django.db.models.fields.IntegerField', [], {})
        },
        'simas.organizaciones': {
            'Meta': {'object_name': 'Organizaciones'},
            'celular': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'correo_electronico': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Departamento']", 'null': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('monitoreo.simas.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sitio_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'simas.recolector': {
            'Meta': {'object_name': 'Recolector'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['indicador19']
