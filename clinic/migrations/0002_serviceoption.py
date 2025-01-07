# Generated by Django 4.2.17 on 2025-01-07 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.PositiveIntegerField(help_text='Duration in minutes')),
                ('price', models.DecimalField(decimal_places=2, help_text='Price in USD', max_digits=6)),
                ('description', models.TextField(help_text='A unique description for this service option')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='clinic.service')),
            ],
        ),
    ]