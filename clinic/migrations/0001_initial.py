# Generated by Django 4.2.17 on 2025-01-07 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the name of the service.', max_length=100, unique=True)),
                ('description', models.TextField(help_text='Provide a brief description of the service.')),
                ('is_active', models.BooleanField(default=True, help_text='Uncheck to deactivate this service.')),
                ('slug', models.SlugField(blank=True, help_text='Auto-generated from the service name.', unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
