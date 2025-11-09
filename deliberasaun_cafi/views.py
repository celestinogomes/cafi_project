from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from deliberasaun_cafi.models import *
from django.contrib import messages
from deliberasaun_cafi.forms import *
from django.utils import timezone
from datetime import datetime
from cafi_project.decorators import allowed_users
from natsort import natsorted

@login_required
@allowed_users(allowed_roles=['admin','staff'])
def deliberasaun(request):
    month = request.GET.get('month')
    year = request.GET.get('year')

    obj = Deliberasaun.objects.all()
    objs = natsorted(obj, key=lambda x: x.no_cafi)
    del_count = obj.count()
    current_month = datetime.now().month
    del_month = obj.filter(data_cafi__month=current_month).count()

    context = {
        'title' : 'Deliberasaun CAFI',
        'obj' : objs,
        'del_month' : del_month,
        'obj_count' : del_count,
    }
    return render(request, 'deliberasaun.html', context)

@login_required
@allowed_users(allowed_roles=['admin'])
def addDeliberasaun(request):
    if request.method == 'POST':
        form = DeliberasaunForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Ita-boot aumenta deliberasaun ho susessu')
            return redirect('deliberasaun')
        else:
            print(form.errors)
    else:
        form = DeliberasaunForm()
    context = {
        'title' : 'Aumenta Deliberasaun | CAFI',
        'form' : form,
    }
    return render(request, 'adddeliberasaun.html', context)

@login_required
def detailDeliberasaun(request, id):
    obj = Deliberasaun.objects.get(no_cafi=id)
    context = {
        'title' : 'Detail Deliberasaun | CAFI',
        'obj' : obj,
    }
    return render(request, 'detaildeliberasaun.html', context)

@login_required
def editDeliberasaun(request, id):
    obj = Deliberasaun.objects.get(no_cafi=id)
    if request.method == 'POST':
        form = DeliberasaunForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Ita-boot altera deliberasaun ho susessu')
            return redirect('deliberasaun')
        else:
            print(form.errors)
    else:
        form = DeliberasaunForm(instance=obj)
    context = {
        'title' : 'Edit Deliberasaun | CAFI',
        'form' : form,
    }
    return render(request, 'addDeliberasaun.html', context)

@login_required
def deleteDeliberasaun(request, id):
    obj = Deliberasaun.objects.get(no_cafi=id)
    obj.delete()
    messages.error(request, f"Ita-boot hamoos deliberasaun {obj} ho susesu!")
    return redirect('deliberasaun')