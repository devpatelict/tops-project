# Generated by Django 4.1 on 2022-09-20 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='payment_status',
            field=models.BooleanField(default=False),
        ),
    ]
