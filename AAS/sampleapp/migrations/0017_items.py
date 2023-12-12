# Generated by Django 4.1.7 on 2023-05-06 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0016_delete_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.TextField()),
                ('cost', models.TextField()),
                ('photo', models.ImageField(null=True, upload_to='pics')),
            ],
            options={
                'db_table': 'items',
            },
        ),
    ]
