# Generated by Django 4.1.7 on 2023-05-06 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0011_alter_items_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='photo',
            field=models.FileField(upload_to=''),
        ),
    ]
