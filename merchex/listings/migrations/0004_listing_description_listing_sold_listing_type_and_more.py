# Generated by Django 4.1.7 on 2023-03-24 09:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_band_active_band_biography_band_genre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='description',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='sold',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='listing',
            name='type',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='year',
            field=models.IntegerField(default=2000, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2023)]),
            preserve_default=False,
        ),
    ]
