from django.shortcuts import render

def landingview(request):
    return render(request, 'landingpage.html')

def supplierslistview(request):
    return render(request, 'supplierslist.html')

def productslistview(request):
    return render(request, 'productslist.html')