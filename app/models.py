# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Address(models.Model):
    member_user = models.OneToOneField('Member', models.CASCADE, primary_key=True)
    house_number = models.CharField(max_length=20, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    town = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        
        db_table = 'ADDRESS'


class Appointment(models.Model):
    appointment_id = models.BigAutoField(primary_key=True)
    caregiver_user = models.ForeignKey('Caregiver', models.CASCADE)
    member_user = models.ForeignKey('Member', models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    work_hours = models.FloatField()
    status = models.CharField(max_length=50)

    class Meta:
        
        db_table = 'APPOINTMENT'


class Caregiver(models.Model):
    caregiver_user = models.OneToOneField('User', models.CASCADE, primary_key=True)
    photo = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    caregiving_type = models.CharField(max_length=100)
    hourly_rate = models.FloatField()

    class Meta:
        
        db_table = 'CAREGIVER'


class Job(models.Model):
    job_id = models.BigAutoField(primary_key=True)
    member_user = models.ForeignKey('Member', models.CASCADE)
    required_caregiving_type = models.CharField(max_length=100)
    other_requirements = models.TextField(blank=True, null=True)
    date_posted = models.DateField()

    class Meta:
        
        db_table = 'JOB'


class JobApplication(models.Model):
    pk = models.CompositePrimaryKey('caregiver_user_id', 'job_id')
    caregiver_user = models.ForeignKey(Caregiver, models.CASCADE)
    job = models.ForeignKey(Job, models.CASCADE)
    date_applied = models.DateField()

    class Meta:
        
        db_table = 'JOB_APPLICATION'


class Member(models.Model):
    member_user = models.OneToOneField('User', models.CASCADE, primary_key=True)
    house_rules = models.TextField(blank=True, null=True)
    dependent_description = models.TextField(blank=True, null=True)

    class Meta:
        
        db_table = 'MEMBER'


class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=255)
    given_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    profile_description = models.TextField(blank=True, null=True)
    password = models.CharField(max_length=255)

    class Meta:
        
        db_table = 'USER'
