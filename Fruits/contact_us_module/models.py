from django.db import models

# Create your models here.






class RequestCall(models.Model):
    full_name = models.CharField(max_length=300,verbose_name='نام و نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل')
    phone_number = models.IntegerField(verbose_name='شماره ی تماس')
    message = models.TextField(verbose_name='پیام')
    called_back = models.BooleanField(default=False,verbose_name='پاسخ داده شده یا خیر؟')
    is_active = models.BooleanField(verbose_name='فعال/غیرفعال')

