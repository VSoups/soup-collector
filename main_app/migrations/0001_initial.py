# Generated by Django 5.0.6 on 2024-05-29 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Soup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('origin', models.CharField(max_length=100)),
                ('temperature', models.CharField(max_length=100)),
                ('broth', models.CharField(max_length=100)),
            ],
        ),
    ]
