# Generated by Django 5.0 on 2023-12-12 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelType', '0004_lesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
