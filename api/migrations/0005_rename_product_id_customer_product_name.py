# Generated by Django 4.1.4 on 2022-12-13 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_sale_total_sale_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='product_id',
            new_name='product_name',
        ),
    ]
