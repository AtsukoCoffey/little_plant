# Generated by Django 3.2.25 on 2025-02-14 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_userprofile_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='full_name',
        ),
    ]
