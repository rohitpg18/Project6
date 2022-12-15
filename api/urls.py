from django.urls import path
from .views import *

urlpatterns = [
    path ('products/' , Products.as_view()),
    # path('products/', ProductListCreate.as_view(), name='products'),
    # path('products/<int:pk>', ProductUpdateDelete.as_view(), name= 'product_update'),
    # path('sales/' , sale_update)
    path('customers/', CustomerList.as_view(), name='customers'),
    # path('customers/<int:pk>', CustomerUpdateDelete.as_view(), name='customer_update'),
    # path("sales/", SaleAPI.as_view()) ,
    # path("<int:product_id>/",sale),
    # path('sale/', get_sale)
]