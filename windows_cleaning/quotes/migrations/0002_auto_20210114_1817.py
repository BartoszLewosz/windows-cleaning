# Generated by Django 2.2.17 on 2021-01-14 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='email',
            field=models.EmailField(error_messages={'required': 'Please enter your phone number'}, max_length=254),
        ),
    ]
