# Generated by Django 3.2.7 on 2021-10-20 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0009_rename_after_saving_z_before_allocate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='z',
            old_name='before_allocate',
            new_name='after_allocate',
        ),
        migrations.RenameField(
            model_name='z',
            old_name='before_saving',
            new_name='after_saving',
        ),
    ]
