# Generated by Django 4.2.19 on 2025-03-16 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Merch",
            fields=[
                ("nome", models.CharField(max_length=200)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
