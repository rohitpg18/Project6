from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=100, unique=True)
    price = models.IntegerField()
    stock = models.IntegerField()
    published_date = models.DateField()
    remaining_stock = models.IntegerField()

    def __str__ (self):
        return f'{self.product_id} {self.product_name}'


class Customer(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE , related_name='product')
    units_sold = models.IntegerField()
    customer_name = models.CharField(max_length=100)
    date_of_sale = models.DateField()
    selling_price = models.IntegerField(default=None)

    def __str__ (self):
        return f'{self.customer_name} - {self.product_id}'
    
    

class Sale(models.Model):
    product_id = models.OneToOneField(Product, on_delete=models.CASCADE , related_name='product_sales')
    total_no_of_sale = models.IntegerField(default=0 , null=True)
    # available_stock_after_sale = models.IntegerField(default=True)
    total_sale_amount = models.IntegerField(default=0, null=True)
    profits = models.IntegerField(null=True, default=0)


@receiver(post_save, sender=Product)
def update_sale_signal(sender, instance, created, **kwargs):
    if created:
        a=Sale.objects.create(product_id=instance)
        a.save()





