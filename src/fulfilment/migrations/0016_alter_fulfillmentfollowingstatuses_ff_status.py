# Generated by Django 5.0.4 on 2024-06-04 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fulfilment', '0015_remove_fulfillmentfollowingstatuses_ff_status_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fulfillmentfollowingstatuses',
            name='ff_status',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
