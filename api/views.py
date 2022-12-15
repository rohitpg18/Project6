from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import views
from rest_framework.views import APIView



# @api_view (['GET'])
# def get_products(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer (products, many = True)
#     return Response (serializer.data)

# @api_view(['POST'])
# def add_prod(request):
#     serializer = ProductSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)

# class ProductListCreate(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class ProductUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

class Products(APIView):
    def get (self, request):
        items = Product.objects.all()
        ser = ProductSerializer (items, many = True)
        return Response (ser.data)


    def post(self , request, format=None):
        serializer = CustomerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            p_id = serializer.data['product_id']
            p_units = serializer.data['units_sold']
            p_price = serializer.data['selling_price']

            product = Product.objects.get(product_id = p_id)
            sales = Sale.objects.get(product_id = p_id)

            product.remaining_stock = product.remaining_stock - int(p_units)

            sales.total_no_of_sale = sales.total_no_of_sale + int(p_units)

            sales.total_sale_amount = sales.total_sale_amount + (int(p_price) * int(p_units))

            sales.profits = (sales.total_no_of_sale * product.price) - sales.total_sale_amount

            product.save()
            sales.save()

            return Response (serializer.data)
        return Response (serializer.errors)








class CustomerList(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# class CustomerUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer


# @api_view (['GET'])
# def get_sale(request):
#     item = Sale.objects.all()
#     serializer = SaleSerializer (item , many=True)
#     return Response (serializer.data)


# @api_view(['POST'])
# def sale(request , product_id):
#     item = Sale.objects.get(pk = product_id)
#     # b = Customer.objects.get(pk = product_id)
#     item.total_no_of_sale = item.total_no_of_sale + 1
#     item.save()
#     print(item.total_no_of_sale)
#     data = SaleSerializer (item , )
#     if data.is_valid():
#         data.save()
#     return Response(data.data)
    


                                                                                                        
    

    







