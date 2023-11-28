from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

def home(request):
    template_name ='core/home.html'
    context = {}
    return render(request, template_name, context)

