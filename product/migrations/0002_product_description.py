# Generated by Django 4.2.3 on 2023-08-01 06:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="description",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
