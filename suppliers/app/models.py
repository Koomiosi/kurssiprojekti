from django.db import models

class Supplier(models.Model):
    companyname = models.CharField(max_length=100, default='firma')
    contactname = models.CharField(max_length=100, default='yhteyshenkilo')
    address = models.CharField(max_length=200, default='osoite')
    phone = models.CharField(max_length=20, default='puhelin')
    email = models.EmailField(max_length=100, default='sahkoposti@esimerkki.com')
    country = models.CharField(max_length=50, default='maa')

class Product(models.Model):
    productname = models.CharField(max_length=100, default='tuote')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, default='kategoria')
    quantityperunit = models.CharField(max_length=50, default='kpl')
    unitprice = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    unitsinstock = models.IntegerField(default=0)
    unitsonorder = models.IntegerField(default=0)
    reorderlevel = models.IntegerField(default=0)
    discontinued = models.BooleanField(default=False)
