# Generated by Django 4.2 on 2023-05-06 11:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_quanity_purchase_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]