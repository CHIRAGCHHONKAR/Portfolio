# Generated by Django 5.0.6 on 2024-07-10 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0002_alter_price_plan_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='plan_logo',
            field=models.CharField(max_length=50),
        ),
    ]
