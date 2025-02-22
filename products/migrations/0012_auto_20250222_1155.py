# Generated by Django 3.2.25 on 2025-02-22 11:55

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20250221_0519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantitem',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, quality=75, scale=None, size=[400, None], upload_to='products'),
        ),
        migrations.AlterField(
            model_name='reviewrating',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, quality=75, scale=None, size=[100, None], upload_to='reviews'),
        ),
    ]
