# Generated by Django 3.2.7 on 2021-10-20 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0011_auto_20211020_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='z_cal',
            name='after_allocate',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='z_cal',
            name='after_saving',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='z_cal',
            name='fix',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='z_cal',
            name='total_varfix',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='z_cal',
            name='var',
            field=models.IntegerField(),
        ),
    ]