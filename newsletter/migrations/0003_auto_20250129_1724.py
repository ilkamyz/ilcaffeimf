# Generated by Django 2.2.12 on 2025-01-29 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_iscrizionenewsletter_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iscrizionenewsletter',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
