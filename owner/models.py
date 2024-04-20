from django.db import models

class Owner(models.Model):
    id = models.CharField(primary_key=True, max_length=36, db_comment='Owner ID')
    contact_id = models.CharField(max_length=36, db_comment='Contact ID')
    fname = models.CharField(max_length=64, db_comment='First name')
    lname = models.CharField(max_length=64, db_comment='Last name')
    status = models.CharField(max_length=5, db_comment='Status')
    crtu = models.CharField(max_length=64, db_comment='Creation User')
    crtd = models.DateTimeField(db_comment='Creation Stamp')
    updu = models.CharField(max_length=64, db_comment='Modification User')
    updd = models.DateTimeField(db_comment='Modification Stamp')

    class Meta:
        managed = False
        db_table = 'owner'
        db_table_comment = 'Owners'

class Contact(models.Model):
    id = models.CharField(primary_key=True, max_length=36, db_comment='Contact ID')
    status = models.CharField(max_length=5, db_comment='Status')
    address1 = models.CharField(max_length=128)
    address2 = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    department = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    zip = models.CharField(max_length=32)
    phone1 = models.CharField(max_length=32)
    phone2 = models.CharField(max_length=32)
    fax = models.CharField(max_length=32)
    email = models.CharField(max_length=128)
    crtu = models.CharField(max_length=64, db_comment='Creation User')
    crtd = models.DateTimeField(db_comment='Creation Stamp')
    updu = models.CharField(max_length=64, db_comment='Modification User')
    updd = models.DateTimeField(db_comment='Modification Stamp')

    class Meta:
        managed = False
        db_table = 'contact'
        db_table_comment = 'Contacts'
