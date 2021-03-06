# Generated by Django 3.0.4 on 2020-06-13 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmodel',
            name='genre',
            field=models.ManyToManyField(related_name='book', to='app.Genre', verbose_name='Раздел'),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='rating',
            field=models.ManyToManyField(related_name='book', to='app.Rating', verbose_name='Рейтинг'),
        ),
    ]
