# Generated by Django 4.1.2 on 2022-10-19 16:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fruit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fruit_name', models.CharField(db_index=True, max_length=300, verbose_name='نام میوه')),
                ('fruit_image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='عکس میوه')),
                ('fruit_price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='قیمت میوه')),
                ('fruit_remaining', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='باقیمانده')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال/غیرفعال')),
            ],
        ),
    ]