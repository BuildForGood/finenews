# Generated by Django 5.1.6 on 2025-03-06 11:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocalNewsSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('domain', models.CharField(max_length=255, unique=True)),
                ('Owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_sites', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
