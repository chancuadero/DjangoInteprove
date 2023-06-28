from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=15,null=False, primary_key=True)
    password = models.CharField(max_length=15, null=False)
    firstname = models.CharField(max_length=15, null=False)
    lastname = models.CharField(max_length=15, null=False)
    type = models.CharField(max_length=1, null=False)


class Investor(models.Model):
    investorprofileid = models.AutoField(null=False, primary_key=True)
    profilename = models.TextField(max_length=255, null=False)
    profiletype = models.TextField(max_length=255, null=False)
    status = models.CharField(max_length=20, null=False, default = 'Not Started')
    taskid = models.CharField(max_length=20,null=True)
    date = models.DateField()
    allocated = models.CharField(max_length=20, null=False, default='No')
    aum = models.CharField(max_length=50, null=False, default=0)
    aa = models.TextField(max_length=50, null=False,default='none')
    custodian = models.CharField(max_length=50, null=False,default='none')
    auditor = models.CharField(max_length=50, null=False,default='none')
    actuary = models.CharField(max_length=50, null=False,default='none')
    leadconsultant = models.CharField(max_length=50, null=False,default='none')
    mcontact = models.CharField(max_length=50, null=False,default='none')
    email = models.CharField(max_length=50, null=False,default='none')


class Project(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    investorprofileid = models.ForeignKey(Investor, on_delete=models.CASCADE)
    projectid = models.AutoField(null=False, primary_key=True)
    projectname = models.CharField(max_length=255, null=False, default='Tier 8')

class Updates(models.Model):
    updateid = models.AutoField(null=False, primary_key=True)
    category = models.CharField(max_length=255, null=False)
    notes = models.TextField(max_length=100, null=False)
    date = models.DateField()