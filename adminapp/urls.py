from django.urls import path
from adminapp import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('profile/', views.profile_view, name='profile'),
    path('settings/', views.settings_view, name='settings'),
    
    # User Management URLs
    path('users/', views.user_list_view, name='user-list'),
    path('users/add/', views.add_user_view, name='add-user'),
    path('users/<int:user_id>/', views.user_detail_view, name='user-detail'),
    path('users/<int:user_id>/reset-password/', views.reset_password_view, name='reset-password'),
]