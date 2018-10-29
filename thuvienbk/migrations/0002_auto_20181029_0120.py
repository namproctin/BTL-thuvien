# Generated by Django 2.0.7 on 2018-10-29 04:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thuvienbk', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='danhgiasach',
            name='rating',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
