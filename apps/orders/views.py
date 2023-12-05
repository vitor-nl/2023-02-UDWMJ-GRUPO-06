from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .serializer import OrderSerializer, OrderItemSerializer
from .models import Order, OrderItem
from .forms import OrderForm, OrderItemForm

# Create your views here.

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer  

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

def add_order(request):
    template_name = 'orders/add_order.html'
    context = {}
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('orders:list_orders')
    form = OrderForm()
    context['form'] = form
    return render(request, template_name, context)


def list_orders(request):
    template_name = 'orders/list_orders.html'
    orders = Order.objects.filter()
    context = {
        'orders': orders
    }
    return render(request, template_name, context)

def edit_order(request, id_order):
    template_name = 'orders/add_order.html'
    context = {}
    order = get_object_or_404(Order, id =id_order)
    if request.method =='POST':
        form = OrderForm(request.POST, instance = order)
        if form.is_valid():
            form.save()
            return redirect('orders:list_orders')
    form = OrderForm(instance=order)
    context['form'] = form
    return render(request, template_name, context)

def delete_order(request, id_order):
    order = Order.objects.get(id=id_order)
    order.delete()
    return redirect('orders:list_orders')

#=======================================================================================================================================================================

def add_orderItem(request):
    template_name = 'orders/add_orderItem.html'
    context = {}
    if request.method == 'POST':
        form = OrderItemForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('/pedidos_itens/')
    form = OrderItemForm()
    context['form'] = form
    return render(request, template_name, context)


def list_orderItens(request):
    template_name = 'orders/list_orderItens.html'
    orderItems = OrderItem.objects.all()  
    context = {
        'orderItems': orderItems  
    }
    return render(request, template_name, context)

def edit_orderItem(request, id_orderItem):
    template_name = 'orders/add_orderItem.html'
    context = {}
    orderItem = get_object_or_404(OrderItem, id=id_orderItem) 
    if request.method == 'POST':
        form = OrderItemForm(request.POST, instance=orderItem) 
        if form.is_valid():
            form.save()
            return redirect('/pedidos_itens/')
    form = OrderItemForm(instance=orderItem)
    context['form'] = form
    return render(request, template_name, context)

def delete_orderItem(request, id_orderItem):
    orderItem = OrderItem.objects.get(id=id_orderItem)
    orderItem.delete()
    return redirect('/pedidos_itens/')