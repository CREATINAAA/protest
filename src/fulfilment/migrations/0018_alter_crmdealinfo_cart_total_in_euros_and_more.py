# Generated by Django 5.0.4 on 2024-06-07 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fulfilment', '0017_rename_item_price_crmdealitem_price_in_euros_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crmdealinfo',
            name='cart_total_in_euros',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='crmdealitem',
            name='price_in_euros',
            field=models.FloatField(),
        ),
    ]
