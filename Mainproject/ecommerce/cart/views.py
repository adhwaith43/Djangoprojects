from django.shortcuts import redirect, render
from django.views import View

from shop.models import Product
from cart.models import Cart

# Create your views here.

class AddToCart(View): # to add to cart
    def get(self,request,i):
        p=Product.objects.get(id=i)
        u=request.user # logged in user
        try:
            c=Cart.objects.get(user=u,product=p) # check whether product is
                                                 #  already placed into the cart table by the user
            
            c.quantity+=1                        # if yes increase the quantity by 1
            c.save()
        except:
            c=Cart.objects.create(user=u,product=p,quantity=1) # if not,creates a new record with quantity 1
            c.save()
        return redirect('cart:cartview')

        

class CartView(View):  # to display cart items selected by the current user
    def get(self,request):
        u=request.user # current user
        c=Cart.objects.filter(user=u)  # reads all items selected by the current user
        context={'cart':c}
        return render(request,'cart.html',context)
    
class CartDecrement(View):  # to decrease quantity of a cart item
    def get(self,request,i):
        try:
            c=Cart.objects.get(id=i)
            if c.quantity > 1:
                c.quantity-=1
                c.save()
            else:
                c.delete()
        except:
            pass

        
        return redirect('cart:cartview')

class CartDelete(View):  # to delete a cart item
    def get(self,request,i):
        try:
            c=Cart.objects.get(id=i)
            c.delete()
        except:
            pass
        return redirect('cart:cartview')