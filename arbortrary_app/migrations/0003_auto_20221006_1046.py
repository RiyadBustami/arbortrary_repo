# Generated by Django 2.2.4 on 2022-10-06 07:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('arbortrary_app', '0002_auto_20221006_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tree',
            name='date_planted',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
