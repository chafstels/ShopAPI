# Generated by Django 4.2.3 on 2023-07-18 06:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("category", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(blank=True, primary_key=True, serialize=False),
        ),
    ]