# Generated by Django 4.2.4 on 2023-08-21 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_order_created_at_order_product_order_qty_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
