from django.db import models
from shop.models import Product,CustomUser

class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete =models.CASCADE)
    user=models.ForeignKey(CustomUser,on_delete =models.CASCADE)
    quantity=models.IntegerField()
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

