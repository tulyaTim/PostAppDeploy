# Generated by Django 5.0.7 on 2024-11-13 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0007_remove_message_receiver_remove_message_sender'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
