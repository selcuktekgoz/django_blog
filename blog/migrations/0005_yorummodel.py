# Generated by Django 5.1.5 on 2025-01-16 09:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_yazilarmodel_resim'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='YorumModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yorum', models.TextField()),
                ('olusturulma_tarihi', models.DateTimeField(auto_now_add=True)),
                ('guncellenme_tarihi', models.DateTimeField(auto_now=True)),
                ('yazan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yyorumlar', to=settings.AUTH_USER_MODEL)),
                ('yazi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yorumlar', to='blog.yazilarmodel')),
            ],
            options={
                'verbose_name': 'Yorum',
                'verbose_name_plural': 'Yorumlar',
                'db_table': 'yorum',
            },
        ),
    ]
