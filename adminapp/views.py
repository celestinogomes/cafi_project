from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.core.paginator import Paginator
from deliberasaun_cafi.models import Deliberasaun
from karta_cafi.models import ConviteCafi, AgendaCafi
from cafi_project.decorators import allowed_users
from .forms import ProfileForm, CustomPasswordChangeForm, UserCreateForm
from django.contrib.auth.hashers import check_password, make_password

@login_required
def dashboard(request):
    now = timezone.now()
    current_month = now.month
    current_year = now.year
    last_month = (now - timedelta(days=30))
    
    total_deliberasaun = Deliberasaun.objects.count()
    total_karta_tama = ConviteCafi.objects.count()
    total_karta_sai = AgendaCafi.objects.count()
    
    deliberasaun_this_month = Deliberasaun.objects.filter(
        data_cafi__month=current_month,
        data_cafi__year=current_year
    ).count()
    
    karta_tama_this_month = ConviteCafi.objects.filter(
        data_convite__month=current_month,
        data_convite__year=current_year
    ).count()
    
    karta_sai_this_month = AgendaCafi.objects.filter(
        data_sai__month=current_month,
        data_sai__year=current_year
    ).count()
    
    last_month_date = last_month
    deliberasaun_last_month = Deliberasaun.objects.filter(
        data_cafi__month=last_month_date.month,
        data_cafi__year=last_month_date.year
    ).count()
    
    karta_tama_last_month = ConviteCafi.objects.filter(
        data_convite__month=last_month_date.month,
        data_convite__year=last_month_date.year
    ).count()
    
    karta_sai_last_month = AgendaCafi.objects.filter(
        data_sai__month=last_month_date.month,
        data_sai__year=last_month_date.year
    ).count()
    
    def calculate_percentage_change(current, previous):
        if previous == 0:
            return 100 if current > 0 else 0
        return round(((current - previous) / previous) * 100, 1)
    
    deliberasaun_change = calculate_percentage_change(deliberasaun_this_month, deliberasaun_last_month)
    karta_tama_change = calculate_percentage_change(karta_tama_this_month, karta_tama_last_month)
    karta_sai_change = calculate_percentage_change(karta_sai_this_month, karta_sai_last_month)
    
    files_deliberasaun = Deliberasaun.objects.exclude(Q(file_attachment='') | Q(file_attachment__isnull=True)).count()
    files_karta_tama = ConviteCafi.objects.exclude(Q(file_attachment='') | Q(file_attachment__isnull=True)).count()
    files_karta_sai = AgendaCafi.objects.exclude(Q(file_attachment='') | Q(file_attachment__isnull=True)).count()
    total_files = files_deliberasaun + files_karta_tama + files_karta_sai
    
    recent_deliberasaun = Deliberasaun.objects.order_by('-data_cafi')[:2]
    recent_karta_tama = ConviteCafi.objects.order_by('-data_convite')[:2]
    recent_karta_sai = AgendaCafi.objects.order_by('-data_sai')[:2]
    
    context = {
        'title': 'ADMIN DASHBOARD',
        'total_deliberasaun': total_deliberasaun,
        'total_karta_tama': total_karta_tama,
        'total_karta_sai': total_karta_sai,
        'total_files': total_files,
        'deliberasaun_this_month': deliberasaun_this_month,
        'karta_tama_this_month': karta_tama_this_month,
        'karta_sai_this_month': karta_sai_this_month,
        'deliberasaun_change': deliberasaun_change,
        'karta_tama_change': karta_tama_change,
        'karta_sai_change': karta_sai_change,
        'recent_deliberasaun': recent_deliberasaun,
        'recent_karta_tama': recent_karta_tama,
        'recent_karta_sai': recent_karta_sai,
    }
    return render(request, 'dashboard.html', context)


@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ita-boot nia profile hadia ona ho susesu!')
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user, user=request.user)
    
    context = {
        'title': 'PROFILE',
        'form': form
    }
    return render(request, 'profile.html', context)


@login_required
def settings_view(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important to keep user logged in
            messages.success(request, 'Ita-boot nia password troca ona ho susesu!')
            return redirect('settings')
    else:
        form = CustomPasswordChangeForm(request.user)
    
    context = {
        'title': 'SETTINGS',
        'form': form
    }
    return render(request, 'settings.html', context)


@login_required
@allowed_users(allowed_roles=['admin'])
def add_user_view(request):
    if not request.user.is_staff:
        messages.error(request, 'Ita-boot la iha permisaun atu aumenta user foun.')
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'User "{user.username}" kria ona ho susesu!')
            return redirect('user-list')
    else:
        form = UserCreateForm()
    
    context = {
        'title': 'AUMENTA USER FOUN',
        'form': form
    }
    return render(request, 'add_user.html', context)


@login_required
@allowed_users(allowed_roles=['admin'])
def user_list_view(request):
    if not request.user.is_staff:
        messages.error(request, 'Ita-boot la iha permisaun atu haree lista user.')
        return redirect('dashboard')
    
    search_query = request.GET.get('search', '')
    if search_query:
        users = User.objects.filter(
            Q(username__icontains=search_query) |
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(email__icontains=search_query)
        ).order_by('-date_joined')
    else:
        users = User.objects.all().order_by('-date_joined')
    
    paginator = Paginator(users, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Add password status check for each user
    def is_default_password(user):
        return check_password('password_123', user.password)
    
    # Add password status to each user object
    for user_item in page_obj:
        user_item.is_default_password = is_default_password(user_item)
    
    tot_user_staff = User.objects.filter(groups__name='staff').count()
    tot_user_admin = User.objects.filter(groups__name='admin').count()

    context = {
        'title': 'LISTA USER',
        'page_obj': page_obj,
        'search_query': search_query,
        'total_users': users.count(),
        'tot_user_staff': tot_user_staff,
        'tot_user_admin': tot_user_admin
    }
    return render(request, 'user_list.html', context)


@login_required
@allowed_users(allowed_roles=['admin'])
def user_detail_view(request, user_id):
    if not request.user.is_staff:
        messages.error(request, 'Ita-boot la iha permisaun atu haree detallu user.')
        return redirect('dashboard')
    
    user_detail = get_object_or_404(User, id=user_id)
    
    # Check if password is default
    is_default_password = check_password('password_123', user_detail.password)
    
    context = {
        'title': f'USER DETALLU - {user_detail.username}',
        'user_detail': user_detail,
        'is_default_password': is_default_password
    }
    return render(request, 'user_detail.html', context)

@login_required
@allowed_users(allowed_roles=['admin'])
def reset_password_view(request, user_id):
    if not request.user.is_staff:
        messages.error(request, 'Ita-boot la iha permisaun atu reset password user.')
        return redirect('user-list')
    user = get_object_or_404(User, id=user_id)
    password = 'password_123'
    hashed_password = make_password(password)
    user.password = hashed_password
    user.save()
    messages.success(request, f'Password ba user "{user.username}" reset ona ho susesu!')
    return redirect('user-list')

