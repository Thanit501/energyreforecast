# Generated by Django 3.2.7 on 2021-10-25 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0016_alter_z_make_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='cal',
            table='predict_Cal',
        ),
        migrations.AlterModelTable(
            name='make',
            table='predict_Make',
        ),
    ]
