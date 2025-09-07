from django.shortcuts import render
from .models import Supplier, Product

def landingview(request):
    return render(request, 'landingpage.html')

def supplierslistview(request):
    supplierlist = Supplier.objects.all()
    context = {'suppliers': supplierlist}
    return render(request, 'supplierslist.html', context)

def productslistview(request):
    productlist = Product.objects.all()
    supplierlist = Supplier.objects.all()
    context = {'products': productlist, 'suppliers': supplierlist}
    return render(request, 'productslist.html', context)