# Generated by Django 5.1.5 on 2025-01-16 09:09

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20250116_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yazilarmodel',
            name='icerik',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
