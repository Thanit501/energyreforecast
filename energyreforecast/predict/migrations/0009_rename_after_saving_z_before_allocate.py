# Generated by Django 3.2.7 on 2021-10-20 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0008_auto_20211019_2226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='z',
            old_name='after_saving',
            new_name='before_allocate',
        ),
    ]
