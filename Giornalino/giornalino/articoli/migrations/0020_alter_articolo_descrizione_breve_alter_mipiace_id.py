# Generated by Django 4.2.18 on 2025-01-29 18:11

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articoli', '0019_auto_20250129_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articolo',
            name='descrizione_breve',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='mipiace',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
