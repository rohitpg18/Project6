# Generated by Django 4.1.4 on 2022-12-13 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_remove_sale_total_sale_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='available_stock_after_sale',
            field=models.IntegerField(default=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='total_no_of_sale',
            field=models.IntegerField(default=0),
        ),
    ]
