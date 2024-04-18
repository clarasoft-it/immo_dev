from django.db import models

# Create your models here.


# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Building(models.Model):
    id = models.CharField(primary_key=True, max_length=36, db_comment='Building ID')
    name = models.CharField(unique=True, max_length=128, db_comment='Building name')
    no = models.CharField(max_length=32, db_comment='Street number')
    street = models.CharField(max_length=128, db_comment='Street name')
    city = models.CharField(max_length=128, db_comment='City')
    department = models.CharField(max_length=128, db_comment='Prov/State/Department')
    country = models.CharField(max_length=128, db_comment='Country')
    zip = models.CharField(max_length=32, db_comment='Postal code')
    crtu = models.CharField(max_length=64, db_comment='Creation User')
    crtd = models.DateTimeField(db_comment='Creation Stamp')
    updu = models.CharField(max_length=64, db_comment='Modification USer')
    updd = models.DateTimeField(db_comment='Modification Stamp')

    class Meta:
        managed = False
        db_table = 'building'
        unique_together = (('no', 'street', 'city', 'department', 'country'),)
        db_table_comment = 'Buildings'

class BuildingOwner(models.Model):
    building = models.OneToOneField('Unit', models.DO_NOTHING, primary_key=True, db_comment='Building ID')  # The composite primary key (building_id, unit_name, owner_id) found, that is not supported. The first column is selected.
    unit_name = models.CharField(max_length=32, db_comment='Unit name')
    owner = models.ForeignKey('Owner', models.DO_NOTHING, db_comment='Owner ID')
    start_date = models.DateField(db_comment='Date From')
    end_date = models.DateField(db_comment='Date To')
    active = models.CharField(max_length=1, db_comment='Status')
    crtu = models.CharField(max_length=64, db_comment='Creation User')
    crtd = models.DateTimeField(db_comment='Creation Stamp')
    updu = models.CharField(max_length=64, db_comment='Modification User')
    updd = models.DateTimeField(db_comment='Modification Stamp')

    class Meta:
        managed = False
        db_table = 'building_owner'
        unique_together = (('building', 'unit_name', 'owner'), ('building', 'unit_name', 'owner'),)
        db_table_comment = 'Building Owners'

class Exercice(models.Model):
    building = models.OneToOneField(Building, models.DO_NOTHING, primary_key=True, db_comment='Building ID')  # The composite primary key (building_id, year) found, that is not supported. The first column is selected.
    year = models.CharField(max_length=4, db_comment='Year')
    month_start = models.CharField(max_length=2, db_comment='Starting month (01, 02, etc)')
    day_start = models.CharField(max_length=2, db_comment='Starting monthly day (01, 02, etc)')
    num_periods = models.CharField(max_length=2, db_comment='Number of monthly periods')
    crtu = models.CharField(max_length=64, db_comment='Creation User')
    crtd = models.DateTimeField(db_comment='Creation Stamp')
    updu = models.CharField(max_length=64, db_comment='Modification User')
    updd = models.DateTimeField(db_comment='Modification Stamp')

    class Meta:
        managed = False
        db_table = 'exercice'
        unique_together = (('building', 'year'), ('building', 'year'),)
        db_table_comment = 'Accounting Exercices'

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

class Unit(models.Model):
    building = models.OneToOneField(Building, models.DO_NOTHING, primary_key=True, db_comment='Building ID')  # The composite primary key (building_id, name) found, that is not supported. The first column is selected.
    name = models.CharField(max_length=32, db_comment='Unit name')
    active = models.CharField(max_length=1, db_comment='Active T/F')
    crtu = models.CharField(max_length=64, db_comment='Creation User')
    crtd = models.DateTimeField(db_comment='Creation Stamp')
    updu = models.CharField(max_length=64, db_comment='Modification User')
    updd = models.DateTimeField(db_comment='Modification Stamp')

    class Meta:
        managed = False
        db_table = 'unit'
        unique_together = (('building', 'name'), ('building', 'name'),)
        db_table_comment = 'Units'
