# Generated by Django 4.0.3 on 2023-10-06 18:32

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(default=accounts.models.generate_random_nickname, max_length=20, unique=True),
        ),
    ]
