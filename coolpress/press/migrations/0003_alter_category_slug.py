# Generated by Django 3.2.9 on 2021-11-05 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('press', '0002_auto_20211019_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
