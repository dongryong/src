from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=220)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

class Purchase(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    quanity = models.PositiveIntegerField()
    