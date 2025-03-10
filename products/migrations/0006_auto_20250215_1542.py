# Generated by Django 3.2.25 on 2025-02-15 15:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_plantitem_sale_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantitem',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='plantitem',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
