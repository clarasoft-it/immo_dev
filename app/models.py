from django.db import models

# Create your models here.

class Application(models.Model):
    id = models.CharField(primary_key=True, max_length=36, db_comment='Applciation ID')
    desc_s = models.CharField(max_length=32, db_comment='Short description')
    desc_l = models.CharField(max_length=64, db_comment='Long description')
    crtu = models.CharField(max_length=64, db_comment='Creation User')
    crtd = models.DateTimeField(db_comment='Creation Stamp')
    updu = models.CharField(max_length=64, db_comment='Modification User')
    updd = models.DateTimeField(db_comment='Modification Stamp')

    class Meta:
        managed = False
        db_table = 'application'
        db_table_comment = 'Applications'

class Language(models.Model):
    id = models.CharField(primary_key=True, max_length=36, db_comment='Language ID')
    desc_s = models.CharField(max_length=32, db_comment='Short description')
    desc_l = models.CharField(max_length=64, db_comment='Long description')
    crtu = models.CharField(max_length=64, db_comment='Creation User')
    crtd = models.DateTimeField(db_comment='Creation Stamp')
    updu = models.CharField(max_length=64, db_comment='Modification User')
    updd = models.DateTimeField(db_comment='Modification Stamp')

    class Meta:
        managed = False
        db_table = 'language'
        db_table_comment = 'Languages'

class Caption(models.Model):
    id = models.CharField(primary_key=True, max_length=36, db_comment='Caption ID')  # The composite primary key (id, app_id, lang_id) found, that is not supported. The first column is selected.
    app = models.ForeignKey(Application, models.DO_NOTHING, db_comment='Application ID')
    lang = models.ForeignKey('Language', models.DO_NOTHING, db_comment='Language ID')
    caption = models.CharField(max_length=255, db_comment='Caption')
    crtu = models.CharField(max_length=64, db_comment='Creation User')
    crtd = models.DateTimeField(db_comment='Creation Stamp')
    updu = models.CharField(max_length=64, db_comment='Modification User')
    updd = models.DateTimeField(db_comment='Modification Stamp')

    class Meta:
        managed = False
        db_table = 'caption'
        unique_together = (('id', 'app', 'lang'), ('lang', 'app', 'id'),)
        db_table_comment = 'Languages'

