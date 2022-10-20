from django.db import models

# Create your models here.



class about(models.Model):
    title = models.CharField(max_length=300,verbose_name='موضوع')
    text1 =  models.TextField(verbose_name='متن اول')
    text2 =  models.TextField(verbose_name='متن دوم')
    about_image = models.ImageField(verbose_name='عکس درباره')
    