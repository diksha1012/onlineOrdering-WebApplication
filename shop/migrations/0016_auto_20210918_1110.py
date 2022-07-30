# Generated by Django 3.2.5 on 2021-09-18 05:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20210918_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 9, 18, 11, 10, 14, 853521)),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product'),
        ),
    ]