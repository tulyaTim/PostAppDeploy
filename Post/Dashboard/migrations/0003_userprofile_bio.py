# Generated by Django 5.0.7 on 2024-10-06 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0002_userprofile_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]