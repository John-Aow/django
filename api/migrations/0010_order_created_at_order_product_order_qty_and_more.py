# Generated by Django 4.2.4 on 2023-08-18 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_remove_order_created_at_remove_order_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.product'),
        ),
        migrations.AddField(
            model_name='order',
            name='qty',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='updated_at',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='OrderDetail',
        ),
    ]
