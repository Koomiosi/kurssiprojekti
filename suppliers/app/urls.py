

from django.urls import path

from .views import landingview,supplierslistview,productslistview,addsupplier


urlpatterns = [
    path('', landingview),

    path('suppliers/', supplierslistview),
    
    path('products/', productslistview),

    path('add-supplier/', addsupplier)
]
