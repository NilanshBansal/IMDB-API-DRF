# Generated by Django 3.1 on 2020-08-22 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imdbapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Movies',
            new_name='Movie',
        ),
    ]
