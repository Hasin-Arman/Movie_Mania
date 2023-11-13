# Generated by Django 4.2.3 on 2023-11-04 04:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('rating', models.IntegerField(default=0)),
                ('text', models.CharField(max_length=250)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.moviemodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]