# Generated by Django 3.1.3 on 2020-12-05 02:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0012_auto_20201205_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_model',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 5, 8, 11, 55, 574063)),
        ),
        migrations.AlterField(
            model_name='exam_model',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 5, 8, 11, 55, 574063)),
        ),
    ]
