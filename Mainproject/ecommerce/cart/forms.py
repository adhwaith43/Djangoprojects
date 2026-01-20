from django import forms

from cart.models import Order

class OrderForm(forms.ModelForm):
    payment_methods=(
        ('COD','Cash On Delivery'), 
        ('Online','Online Payment'))
    payment_method=forms.ChoiceField(choices=payment_methods,widget=forms.RadioSelect)
    class Meta:
        model=Order
        fields=['address','phone','payment_method']
