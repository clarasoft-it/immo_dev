from django.db import models

class Contact(models.Model):
    id = models.CharField(primary_key=True, max_length=36, db_comment='Contact ID')
    status = models.CharField(max_length=5, db_comment='Activity tatus')
    fname = models.CharField(max_length=64, db_comment='First name')
    lname = models.CharField(max_length=64, db_comment='Last name')
    address1 = models.CharField(max_length=128, db_comment='Address 1')
    address2 = models.CharField(max_length=128, db_comment='Address 2')
    city = models.CharField(max_length=128, db_comment='City')
    department = models.CharField(max_length=128, db_comment='Prov/State/Department')
    country = models.CharField(max_length=128, db_comment='Country')
    zip = models.CharField(max_length=32, db_comment='Postal code')
    phone1 = models.CharField(max_length=32, db_comment='Phone 1')
    phone2 = models.CharField(max_length=32, db_comment='Phone 2')
    fax = models.CharField(max_length=32, db_comment='Fax')
    email = models.CharField(max_length=128, db_comment='Email')
    crtu = models.CharField(max_length=64, db_comment='Creation User')
    crtd = models.DateTimeField(db_comment='Creation Stamp')
    updu = models.CharField(max_length=64, db_comment='Modification User')
    updd = models.DateTimeField(db_comment='Modification Stamp')

    class Meta:
        managed = False
        db_table = 'contact'
        db_table_comment = 'Contacts'

class Owner(models.Model):
    id = models.CharField(primary_key=True, max_length=36, db_comment='Owner ID')
    status = models.CharField(max_length=5, db_comment='Activity status')
    crtu = models.CharField(max_length=64, db_comment='Creation User')
    crtd = models.DateTimeField(db_comment='Creation Stamp')
    updu = models.CharField(max_length=64, db_comment='Modification User')
    updd = models.DateTimeField(db_comment='Modification Stamp')

    class Meta:
        managed = False
        db_table = 'owner'
        db_table_comment = 'Owners'
