# Generated by Django 4.2.4 on 2023-08-21 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_shipment_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='recieved_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='shipment_date',
            field=models.DateField(),
        ),
    ]