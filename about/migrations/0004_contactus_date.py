# Generated by Django 3.2.25 on 2025-02-18 12:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_auto_20250218_0218'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
