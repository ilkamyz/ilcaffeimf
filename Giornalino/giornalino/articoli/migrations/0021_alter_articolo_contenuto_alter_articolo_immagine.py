# Generated by Django 4.2.18 on 2025-01-29 18:16

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articoli', '0020_alter_articolo_descrizione_breve_alter_mipiace_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articolo',
            name='contenuto',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='articolo',
            name='immagine',
            field=models.ImageField(blank=True, null=True, upload_to='articoli/'),
        ),
    ]
