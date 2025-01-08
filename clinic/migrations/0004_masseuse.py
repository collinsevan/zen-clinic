# Generated by Django 4.2.17 on 2025-01-07 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0003_alter_serviceoption_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Masseuse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6)),
            ],
        ),
    ]