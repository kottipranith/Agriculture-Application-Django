# Generated by Django 4.1.7 on 2023-04-01 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0003_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='is_admin',
            field=models.BooleanField(default=None),
        ),
    ]
