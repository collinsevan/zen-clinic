# Generated by Django 4.2.17 on 2025-01-07 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0002_serviceoption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceoption',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='Price in Euro(€)', max_digits=6),
        ),
    ]