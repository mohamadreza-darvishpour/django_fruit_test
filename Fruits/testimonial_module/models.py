from django.db import models

# Create your models here.


class testimonial(models.Model):
    image_testimonial = models.ImageField(verbose_name = 'عکس گواهینامه')
    user_name = models.CharField(max_length=300,verbose_name='نام و نام خانوادگی')
    short_description = models.CharField(max_length=400,verbose_name='توضیحات کوتاه')
    description = models.TextField(verbose_name='توضیحات')
    is_active = models.BooleanField(default=True,verbose_name='فعال/غیرفعال')
    is_deleted = models.BooleanField(default=False,verbose_name='حذف شده/نشده')