# Generated by Django 3.2.5 on 2021-09-11 11:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20210831_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 9, 11, 16, 37, 52, 777895)),
        ),
    ]
