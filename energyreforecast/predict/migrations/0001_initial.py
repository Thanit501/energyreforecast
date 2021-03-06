# Generated by Django 3.2.7 on 2021-09-29 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Z',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_range', models.CharField(max_length=150)),
                ('month_predict', models.CharField(max_length=150)),
                ('production', models.IntegerField()),
                ('working_day', models.IntegerField()),
                ('allocate', models.IntegerField()),
                ('saving', models.IntegerField()),
            ],
            options={
                'db_table': 'predict_z',
            },
        ),
        migrations.CreateModel(
            name='Z_DALIY',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=150)),
                ('production_day', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Z_MAKE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(default=None, max_length=150)),
                ('production_month', models.IntegerField()),
                ('energy_month', models.IntegerField()),
                ('working_day', models.IntegerField()),
                ('var', models.IntegerField()),
                ('fix', models.IntegerField()),
                ('total_varfix', models.IntegerField()),
                ('tech_ratio', models.FloatField()),
            ],
        ),
    ]
