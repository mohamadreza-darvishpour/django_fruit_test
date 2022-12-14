# Generated by Django 4.1.2 on 2022-10-20 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_testimonial', models.ImageField(upload_to='', verbose_name='عکس گواهینامه')),
                ('user_name', models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')),
                ('short_description', models.CharField(max_length=400, verbose_name='توضیحات کوتاه')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال/غیرفعال')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='حذف شده/نشده')),
            ],
        ),
    ]
