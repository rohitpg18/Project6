# Generated by Django 4.1.4 on 2022-12-14 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_rename_product_id_customer_product_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='product',
            new_name='product_id',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='id',
            new_name='product_id',
        ),
        migrations.RenameField(
            model_name='sale',
            old_name='product',
            new_name='product_id',
        ),
    ]
