# Generated by Django 4.2.17 on 2025-01-16 22:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articoli', '0005_alter_articolo_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='articolo',
            name='ora_pubblicazione',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
