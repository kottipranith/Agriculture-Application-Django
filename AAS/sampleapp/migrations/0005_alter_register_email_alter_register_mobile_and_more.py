# Generated by Django 4.1.7 on 2023-05-06 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0004_register_is_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='register',
            name='mobile',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='register',
            name='password',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='register',
            name='username',
            field=models.TextField(max_length=50),
        ),
    ]
