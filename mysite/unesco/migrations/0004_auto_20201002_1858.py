# Generated by Django 3.1.1 on 2020-10-02 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unesco', '0003_auto_20201002_1811'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sites',
            new_name='Site',
        ),
        migrations.RenameModel(
            old_name='States',
            new_name='State',
        ),
    ]
