from django.db import models
from django.utils import timezone

SORTING_CHOICES = ( 
    ("activity", "activity"), 
    ("creation", "creation"), 
    ("votes", "votes"), 
    ("relevance", "relevance"), 
    )
ORDER_CHOICES = ( 
    ("asc", "asc"), 
    ("desc", "desc"), 
    )

class Questions(models.Model):
    page= models.IntegerField(default=None,null=True,blank=True)
    pagesize= models.IntegerField(default=None,null=True,blank=True)
    fromdate= models.DateField(default=None,null=True,blank=True)
    todate= models.DateField(default=None,null=True,blank=True)
    min= models.DateField(default = None, null = True,blank=True)
    max= models.DateField(default = None, null = True,blank=True)
    sort= models.CharField(max_length= 30,choices=SORTING_CHOICES, default = None, null = True,blank=True)
    q= models.CharField(max_length=1000,default = None, null = True,blank=True)
    accepted= models.BooleanField(default = False, null = True,)
    answers= models.IntegerField(default = None, null = True,blank=True)
    body= models.CharField(max_length=1000,default = None, null = True,blank=True)
    closed= models.BooleanField(default = False, null = True,)
    migrated= models.BooleanField(default = False, null = True,)
    notice= models.BooleanField(default = False, null = True,)
    nottagged= models.CharField(max_length=1000,default = None, null = True,blank=True)
    tagged= models.CharField(max_length=1000,default = None, null = True,blank=True)
    title= models.CharField(max_length=1000,default = None, null = True,blank=True)
    user= models.IntegerField(default = None, null = True,blank=True)
    url= models.CharField(max_length=1000,default = None, null = True,blank=True)
    views= models.IntegerField(default = None, null = True,blank=True)
    wiki= models.BooleanField(default = False, null = True,)
    site= "stackoverflow"

    def __str__(self):
        return self.site