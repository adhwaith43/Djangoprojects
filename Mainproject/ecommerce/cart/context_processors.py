from cart.models import Cart

def cart(request):
    count=0


    if request.user.is_authenticated:
        u=request.user
        try:
            c=Cart.objects.filter(user=u)
            sum=0
            for i in c:
                sum+=i.quantity
            count=sum
        except:
            count=0
    
    return {'count': count}

