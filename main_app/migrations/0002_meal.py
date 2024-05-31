# Generated by Django 5.0.6 on 2024-05-31 20:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=100)),
                ('rating', models.CharField(choices=[('ON', 1), ('TW', 2), ('TH', 3), ('FO', 4), ('FI', 5)], default='ON', max_length=2)),
                ('soup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.soup')),
            ],
        ),
    ]
