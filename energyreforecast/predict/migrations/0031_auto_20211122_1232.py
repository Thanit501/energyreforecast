# Generated by Django 3.2.9 on 2021-11-22 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0030_auto_20211118_1038'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Make',
        ),
        migrations.DeleteModel(
            name='Z_Cal',
        ),
        migrations.DeleteModel(
            name='Z_MAKE',
        ),
    ]
