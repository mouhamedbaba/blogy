# Generated by Django 4.2.6 on 2023-10-24 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sudo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='favicon',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
