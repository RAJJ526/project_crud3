from django.shortcuts import render, redirect
from .models import *
from .forms import *
def index(request):
    Search=request.GET.get('search')
    if Search:
        obj=Register.objects.filter(name__icontains=Search)
    else:
        obj=Register.objects.all()
    context={
        'obj':obj,
    }
    return render(request, 'index.html', context)

def save_data(request):
    if request.method=="POST":
        obj=Registerform(request.POST)
        if obj.is_valid():
            obj.save()
            return redirect('/')
        else:
            context={'error':obj}
            return render(request, 'add.html', context)
    return render(request, 'add.html')

def delete(request, id):
    Register.objects.get(id=id).delete()
    return redirect('/')

def update(request,id):
    if request.method=="POST":
        x=Register.objects.get(id=id)
        obj=Registerform(request.POST, instance=x)
        if obj.is_valid():
            obj.save()
            return redirect('/')
        else:
            context={'error':obj}
            return render(request, 'update.html', context)
    obj=Register.objects.get(id=id)
    context={
        'obj':obj
    }
    return render(request, 'update.html', context)
# Create your views here.
