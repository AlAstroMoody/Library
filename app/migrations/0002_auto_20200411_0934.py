# Generated by Django 3.0.4 on 2020-04-11 09:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookmodel',
            options={'ordering': ['-time_added'], 'verbose_name': 'Библиотека', 'verbose_name_plural': 'Библиотека'},
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='time_added',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 11, 9, 34, 43, 705676)),
        ),
    ]