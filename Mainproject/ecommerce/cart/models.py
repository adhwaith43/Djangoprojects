from django.db import models
from shop.models import Product,CustomUser

class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete =models.CASCADE)
    user=models.ForeignKey(CustomUser,on_delete =models.CASCADE)
    quantity=models.IntegerField()
    date_added=models.DateTimeField(auto_now_add=True)

    def subtotal(self):
        return self.quantity * self.product.price

    def __str__(self):
        return self.product.name

class Order(models.Model):
    user=models.ForeignKey(CustomUser,on_delete =models.CASCADE)
    address=models.TextField(max_length=100)
    phone=models.CharField(max_length=10)
    amount=models.IntegerField()
    order_id=models.CharField(max_length=200,null=True)
    ordered_date=models.DateTimeField(auto_now_add=True)
    is_ordered=models.BooleanField(default=False)
    delivery_status=models.CharField(default='Pending',max_length=200)
    payment_method=models.CharField(max_length=200)

    def __str__(self):
        return self.user.username

class Order_items(models.Model):
    order=models.ForeignKey(Order,on_delete =models.CASCADE)
    product=models.ForeignKey(Product,on_delete =models.CASCADE)
    quantity=models.IntegerField()

