from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ata_reuniaun.models import *
from django.contrib import messages
from ata_reuniaun.forms import *
from django.utils import timezone
from datetime import datetime
from cafi_project.decorators import allowed_users

@login_required
@allowed_users(allowed_roles=['admin','staff'])
def ata(request):
    month = request.GET.get('month')
    year = request.GET.get('year')

    obj = Ata.objects.all()
    current_month = datetime.now().month
    del_month = obj.filter(data_ata__month=current_month).count()

    context = {
        'title' : 'ata reuniaun',
        'obj' : obj,
        'del_month' : del_month,
    }
    return render(request, 'ata.html', context)

@login_required
@allowed_users(allowed_roles=['admin'])
def addAta(request):
    if request.method == 'POST':
        form = AtaForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Ita-boot aumenta ata ho susessu')
            return redirect('ata')
        else:
            print(form.errors)
    else:
        form = AtaForm()
    context = {
        'title' : 'Aumenta Ata | Reuniaun',
        'form' : form,
    }
    return render(request, 'addata.html', context)

@login_required
def detailAta(request, id):
    obj = Ata.objects.get(id=id)
    context = {
        'title' : 'Detail Ata | Reuniaun',
        'obj' : obj,
    }
    return render(request, 'detailata.html', context)

@login_required
def editAta(request, id):
    obj = Ata.objects.get(id=id)
    if request.method == 'POST':
        form = AtaForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Ita-boot altera ata ho susessu')
            return redirect('ata')
        else:
            print(form.errors)
    else:
        form = AtaForm(instance=obj)
    context = {
        'title' : 'Edit Ata | Reuniaun',
        'form' : form,
    }
    return render(request, 'addAta.html', context)

@login_required
def deleteAta(request, id):
    obj = Ata.objects.get(id=id)
    obj.delete()
    messages.error(request, f"Ita-boot hamoos Ata {obj} ho susesu!")
    return redirect('ata')
# Create your views here.
