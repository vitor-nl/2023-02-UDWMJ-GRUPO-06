from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, ClientSocialnetwork
from rest_framework import viewsets
from .serializer import ClientSerializer, ClientSocialnetworkSerializer
from .forms import ClientForm

# Create your views here.

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer  

class ClientSocialnetworkViewSet(viewsets.ModelViewSet):
    queryset = ClientSocialnetwork.objects.all()
    serializer_class = ClientSocialnetworkSerializer

def add_client(request):
    template_name = 'clients/add_client.html'
    context = {}
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('clients:list_clients')
    form = ClientForm()
    context['form'] = form
    return render(request, template_name, context)

def list_client(request):
    template_name = 'clients/list_clients.html'
    clients = Client.objects.filter()
    context = {
        'clients': clients
    }
    return render(request, template_name, context)

def edit_client(request, id_client):
    template_name = 'clients/add_client.html'
    context ={}
    client = get_object_or_404(Client, id=id_client)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('clients:list_clients')
    form = ClientForm(instance=client)
    context['form'] = form
    return render(request, template_name, context)

def delete_clients(request, id_client):
    client = Client.objects.get(id=id_client)
    client.delete()
    return redirect('clients:list_clients')