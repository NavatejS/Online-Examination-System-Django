# Generated by Django 3.1.3 on 2021-05-19 18:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0019_auto_20210513_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_model',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 19, 23, 57, 8, 281905)),
        ),
        migrations.AlterField(
            model_name='exam_model',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 19, 23, 57, 8, 281884)),
        ),
    ]