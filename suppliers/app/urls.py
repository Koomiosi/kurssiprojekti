

from django.urls import path

from .views import landingview,supplierslistview,productslistview


urlpatterns = [
    path('', landingview),

    path('suppliers/', supplierslistview),
    
    path('products/', productslistview)
]
