# Generated by Django 2.2.3 on 2019-08-09 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_remove_users_number_of_friends'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='recieved_messages',
            field=models.IntegerField(null=True),
        ),
    ]