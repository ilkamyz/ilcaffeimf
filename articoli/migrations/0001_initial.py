# Generated by Django 5.1.4 on 2025-01-12 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articolo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=200)),
                ('contenuto', models.TextField()),
                ('autore', models.CharField(max_length=100)),
                ('data_pubblicazione', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
