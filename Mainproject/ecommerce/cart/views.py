from django.shortcuts import redirect, render
from django.views import View
from cart.forms import OrderForm
from shop.models import Product
from cart.models import Cart

import uuid


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
    # def get(self,request):
    #     u=request.user # current user
    #     c=Cart.objects.filter(user=u)  # reads all items selected by the current user
    #     context={'cart':c}
    #     return render(request,'cart.html',context)


    def get(self,request):
        u=request.user # current user
        c=Cart.objects.filter(user=u)  # reads all items selected by the current user

        total=0
        for i in c:
            total+=i.subtotal()
        context={'cart':c,'total':total}
        return render(request,'cart.html',context)
    
    
    
class CartDecrement(View):  # to decrease quantity of a cart item
    def get(self,request,i):
        p=Product.objects.get(id=i)
        u=request.user # logged in user
        try:
            c=Cart.objects.get(user=u,product=p)
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
        p=Product.objects.get(id=i)
        u=request.user # logged in user
        try:
            c=Cart.objects.get(user=u,product=p)
            c.delete()
        except:
            pass
        return redirect('cart:cartview')

from cart.models import Order_items
import razorpay # import razorpay

class Checkout(View):
    def get(self,request):
        form_instance=OrderForm()
        context={'form':form_instance}
        return render(request,'checkout.html',context)
    
    def post(self,request):
        print(request.POST)
        form_instance=OrderForm(request.POST)
        if form_instance.is_valid():
                o=form_instance.save(commit=False)
                # user
                u=request.user
                o.user=u

                # order amount
                c=Cart.objects.filter(user=u)  
                total=0
                for i in c:
                    total+=i.subtotal()
                print(total)
                o.amount=int(total)
                o.save()

                # payment method
                if(o.payment_method=="Online"):
                    # 1.Razor pay client connection
                    client=razorpay.Client(auth=('rzp_test_S60HMkQsPcr2Os','lykcXlDgvU2HTCW2SDgjTT9c'))
                    print(client)

                    # 2.place order
                    response_payment=client.order.create(dict(amount=o.amount*100,currency='INR')) # (amount*100)converting into paisa for proper displaying
                    print(response_payment)
                    id=response_payment['id']
                    o.order_id=id
                    o.save()
                    context={'payment':response_payment}

                    return render(request,'payment.html',context)
                else:
                    id=uuid.uuid4().hex[:14]
                    o.order_id='order_COD'+id
                    o.is_ordered=True
                    o.save()

                    # Add each item from cart to order_items table
                    for i in c:
                        item=Order_items.objects.create(order=o,product=i.product,quantity=i.quantity)
                        item.save()

                    c.delete()  # to delete  cart

                    return render(request,'payment.html')
