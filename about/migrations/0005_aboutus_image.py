# Generated by Django 4.2 on 2025-02-25 20:14

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_contactus_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, quality=75, scale=None, size=[400, None], upload_to='about'),
        ),
    ]
