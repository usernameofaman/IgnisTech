# Generated by Django 3.1.5 on 2021-02-28 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20210228_1614'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Destination',
            new_name='EventData',
        ),
    ]
