from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .serializer import OrderSerializer, OrderItemSerializer
from .models import Order, OrderItem

# Create your views here.

def add_order(request):
    template_name = 'order/add_order.html'
    context = {}
    if request.method == 'POST':
        form = orderForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('orders:list_orders')
    form = orderForm()
    context['form'] = form
    return render(request, template_name, context)

def list_orders(request):
    template_name = 'orders/list_orders.html'
    orders = Order.objects.filter()
    context = {
        'Orders': orders
    }
    return render(request, template_name, context)

def edit_order(request, id_order):
    template_name = 'order/add_order.html'
    context ={}
    order = get_object_or_404(Order, id=id_order)
    if request.method == 'POST':
        form = orderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('categories:list_categories')
    form = orderForm(instance=order)
    context['form'] = form
    return render(request, template_name, context)

def delete_order(request, id_order):
    order = order.objects.get(id=id_order)
    order.delete()
    return redirect('categories:list_categories')

