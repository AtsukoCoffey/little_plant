# Generated by Django 3.2.25 on 2025-02-18 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_alter_aboutus_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPurpose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='content',
            field=models.TextField(max_length=1000),
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('checked', models.BooleanField(default=False)),
                ('purpose', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='about.contactpurpose')),
            ],
        ),
    ]
