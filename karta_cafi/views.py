from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from karta_cafi.models import *
from karta_cafi.forms import *
from django.contrib import messages

# Karta Tama
@login_required
def kartaTama(request):
    obj = ConviteCafi.objects.all()
    context = {
        'title' : 'Karta Tama CAFI',
        'obj' : obj,
    }
    return render(request, 'karta_tama/list.html', context)

@login_required
def addKTama(request):
    if request.method == 'POST':
        form = KartaTamaForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Ita-boot aumenta Karta Tama ho susessu')
            return redirect('karta-tama')
        else:
            print(form.errors)
    else:
        form = KartaTamaForm()
    context = {
        'title' : 'Aumenta Karta Tama | CAFI',
        'form' : form,
    }
    return render(request, 'karta_tama/add.html', context)

@login_required
def detailkt(request, id):
    obj = ConviteCafi.objects.get(no_karta=id)
    context = {
        'title' : 'Detail Karta Tama | CAFI',
        'obj' : obj,
    }
    return render(request, 'karta_tama/detail.html', context)

@login_required
def editkt(request, id):
    obj = ConviteCafi.objects.get(no_karta=id)
    if request.method == 'POST':
        form = KartaTamaForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Ita-boot altera Informasaun ba karta nian ho susessu')
            return redirect('karta-tama')
        else:
            print(form.errors)
    else:
        form = KartaTamaForm(instance=obj)
    context = {
        'title' : 'Edit Karta | CAFI',
        'form' : form,
    }
    return render(request, 'karta_tama/add.html', context)

@login_required
def deletekt(request, id):
    obj = ConviteCafi.objects.get(no_karta=id)
    obj.delete()
    messages.error(request, f"Ita-boot hamoos ona karta {obj} ho susesu!")
    return redirect('karta-tama')

# Karta Sai
@login_required
def kartasai(request):
    obj = AgendaCafi.objects.all()
    context = {
        'title' : 'Karta Sai CAFI',
        'obj' : obj,
    }
    return render(request, 'karta_sai/list.html', context)

@login_required
def addks(request):
    if request.method == 'POST':
        form = KartaSaiForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Ita-boot aumenta Karta Sai ho susessu')
            return redirect('karta-sai')
        else:
            print(form.errors)
    else:
        form = KartaSaiForm()
    context = {
        'title' : 'Aumenta Karta Sai | CAFI',
        'form' : form,
    }
    return render(request, 'karta_sai/add.html', context)

@login_required
def detailks(request, id):
    obj = AgendaCafi.objects.get(no_karta=id)
    context = {
        'title' : 'Detail Karta Sai | CAFI',
        'obj' : obj,
    }
    return render(request, 'karta_sai/detail.html', context)

@login_required
def editks(request, id):
    obj = AgendaCafi.objects.get(no_karta=id)
    if request.method == 'POST':
        form = KartaSaiForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Ita-boot altera Informasaun ba karta nian ho susessu')
            return redirect('karta-sai')
        else:
            print(form.errors)
    else:
        form = KartaSaiForm(instance=obj)
    context = {
        'title' : 'Edit Karta | CAFI',
        'form' : form,
    }
    return render(request, 'karta_sai/add.html', context)

@login_required
def deleteks(request, id):
    obj = AgendaCafi.objects.get(no_karta=id)
    obj.delete()
    messages.error(request, f"Ita-boot hamoos ona karta {obj} ho susesu!")
    return redirect('karta-sai')