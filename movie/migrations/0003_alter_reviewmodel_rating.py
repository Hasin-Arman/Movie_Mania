# Generated by Django 4.2.3 on 2023-11-05 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_reviewmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewmodel',
            name='rating',
            field=models.PositiveIntegerField(default=0),
        ),
    ]