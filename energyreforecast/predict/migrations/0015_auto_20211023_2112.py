# Generated by Django 3.2.7 on 2021-10-23 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0014_auto_20211023_2111'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='predict_Cal',
            new_name='Cal',
        ),
        migrations.RenameModel(
            old_name='predict_MAKE',
            new_name='Make',
        ),
        migrations.AlterModelTable(
            name='predict',
            table='predict',
        ),
    ]