# Generated by Django 4.1.7 on 2023-05-06 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0026_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='BioData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.TextField()),
                ('lastname', models.TextField()),
                ('dob', models.DateField()),
                ('phone', models.TextField()),
            ],
            options={
                'db_table': 'BioData',
            },
        ),
    ]
