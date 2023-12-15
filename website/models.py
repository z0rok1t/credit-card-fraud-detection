from django.db import models

from django.contrib.auth.models import AbstractUser,Group, Permission



class datasettt(models.Model):
    Time = models.FloatField()
    V1 = models.FloatField()
    V2 = models.FloatField()
    V3 = models.FloatField()
    V4 = models.FloatField()
    V5 = models.FloatField()
    V6 = models.FloatField()
    V7 = models.FloatField()
    V8 = models.FloatField()
    V9 = models.FloatField()
    V10 = models.FloatField()
    V11= models.FloatField()
    V12 = models.FloatField()
    V13 = models.FloatField()
    V14 = models.FloatField()
    V15 = models.FloatField()
    V16 = models.FloatField()
    V17 = models.FloatField()
    V18 = models.FloatField()
    V19 = models.FloatField()
    V20 = models.FloatField()
    V21 = models.FloatField()
    V22 = models.FloatField()
    V23 = models.FloatField()
    V24 = models.FloatField()
    V25 = models.FloatField()
    V26 = models.FloatField()
    V27 = models.FloatField()
    V28 = models.FloatField()
    Amount = models.FloatField()
    Class = models.CharField(max_length=5)
    
    def get_field_value(self, field_num):
        field_name= f'field{field_num}'
        getattr(self, field_name)