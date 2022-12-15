from rest_framework import serializers
from api.models import *
    
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['total_no_of_sale', 'total_sale_amount', 'profits']

class ProductSerializer(serializers.ModelSerializer):
    product_sales = SaleSerializer(many = False , read_only=True)
    class Meta:
        model = Product
        fields = ['product_id', 'product_name', 'stock', 'price', 'published_date', 'remaining_stock' , 'product_sales']
        