from django import forms
from .models import Order, OrderItem
from products.models import Product
from clients.models import Client

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ()

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        exclude = ()