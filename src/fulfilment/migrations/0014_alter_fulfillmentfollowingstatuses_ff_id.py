# Generated by Django 5.0.4 on 2024-06-04 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fulfilment', '0013_fulfillmentfollowingstatuses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fulfillmentfollowingstatuses',
            name='ff_id',
            field=models.CharField(max_length=255),
        ),
    ]
