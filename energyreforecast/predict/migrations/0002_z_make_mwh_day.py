# Generated by Django 3.2.7 on 2021-10-04 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='z_make',
            name='MWh_day',
            field=models.FloatField(default=2),
            preserve_default=False,
        ),
    ]
