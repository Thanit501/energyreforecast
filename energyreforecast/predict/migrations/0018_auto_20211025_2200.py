# Generated by Django 3.2.7 on 2021-10-25 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0017_auto_20211025_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='make',
            name='MWh_day',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='make',
            name='tech_ratio',
            field=models.FloatField(),
        ),
    ]
