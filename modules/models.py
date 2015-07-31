from django.db import models
from django import forms

class installed(models.Model):
    name        = models.CharField(max_length=300)
    active      = models.CharField(max_length=300)
    
    
class vectors(models.Model):
    name        = models.CharField(max_length=300)
    active      = models.CharField(max_length=300)
    
    
class iptrack(models.Model):
    address     = models.CharField(max_length=300)
    mac         = models.CharField(max_length=300)
    os          = models.CharField(max_length=300, default = 'unknown')
    osdetails   = models.CharField(max_length=300)
    injected    = models.CharField(max_length=300)
    expand      = models.CharField(max_length=300, default = '0')
    
    
class scan(models.Model):
    address     = models.CharField(max_length=300)
    ports       = models.CharField(max_length=300)
    osdetails   = models.CharField(max_length=300)
    hostname    = models.CharField(max_length=300)
    scanning    = models.CharField(max_length=300, default = '0')
    
class apgen(models.Model):
    essid       = models.CharField(max_length=300)
    channel     = models.CharField(max_length=300)
    atknic      = models.CharField(max_length=300)
    netnic      = models.CharField(max_length=300)

class arppoison(models.Model):
    target      = models.CharField(max_length=300, default = 'none')
    method      = models.CharField(max_length=300, default = 'none')
    
class sessions(models.Model):
    source      = models.CharField(max_length=300)
    session    = models.CharField(max_length=300)
    date        = models.CharField(max_length=300)
    
