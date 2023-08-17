# Generated by Django 4.2.4 on 2023-08-17 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_order_product_id_remove_order_user_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='shipment',
            old_name='address_id',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='shipment',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='shipmentdetail',
            old_name='order_id',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='shipmentdetail',
            old_name='shipment_id',
            new_name='shipment',
        ),
    ]
