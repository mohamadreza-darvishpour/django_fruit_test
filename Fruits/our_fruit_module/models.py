from ftplib import MAXLINE
from tabnanny import verbose
from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.



class fruit(models.Model):
    fruit_name = models.CharField(max_length=300,verbose_name='نام میوه',db_index=True)
    fruit_image = models.ImageField(null=True,blank=True,verbose_name='عکس میوه')
    fruit_price = models.IntegerField(null=False,blank=False,validators=[MinValueValidator(0),],verbose_name='قیمت میوه')
    fruit_remaining = models.IntegerField(validators=[MinValueValidator(0),],verbose_name='باقیمانده')
    is_active = models.BooleanField(default=True,verbose_name='فعال/غیرفعال')


