# Generated by Django 4.0.4 on 2022-06-14 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='date_projet',
            field=models.DateField(max_length=100, verbose_name='Date projet'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='url',
            field=models.URLField(max_length=100, verbose_name='Url'),
        ),
    ]
