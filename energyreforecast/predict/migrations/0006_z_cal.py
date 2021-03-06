# Generated by Django 3.2.7 on 2021-10-15 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0005_remove_z_energy_predict'),
    ]

    operations = [
        migrations.CreateModel(
            name='Z_Cal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('var', models.FloatField()),
                ('fix', models.FloatField()),
                ('total_varfix', models.FloatField()),
                ('tech_ratio', models.FloatField()),
                ('before_saving', models.FloatField()),
                ('saving', models.FloatField()),
                ('after_saving', models.FloatField()),
                ('energy_predict', models.FloatField()),
            ],
        ),
    ]
