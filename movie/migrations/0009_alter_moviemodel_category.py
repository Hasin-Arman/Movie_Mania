# Generated by Django 4.2.3 on 2023-11-13 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0008_alter_moviemodel_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviemodel',
            name='category',
            field=models.SlugField(choices=[('Thriller', 'Thriller'), ('Sci-fi', 'Sci-fi'), ('Action', 'Action'), ('Horror', 'Horror'), ('Romance', 'Romance'), ('Comedy', 'Comedy')], default='Action', max_length=100),
        ),
    ]
