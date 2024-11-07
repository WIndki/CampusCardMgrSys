# Generated by Django 5.1.3 on 2024-11-07 09:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsys', '0002_alter_user_lastlogin_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bookPrice',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='card',
            name='cardId',
            field=models.CharField(max_length=8, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 8', regex='^.{10}$')]),
        ),
    ]
