# Generated by Django 2.2.3 on 2019-08-09 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='number_of_friends',
        ),
    ]
