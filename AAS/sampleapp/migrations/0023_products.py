# Generated by Django 4.1.7 on 2023-05-06 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0022_delete_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.TextField()),
                ('cost', models.TextField()),
                ('photo', models.ImageField(upload_to='static/images')),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]
