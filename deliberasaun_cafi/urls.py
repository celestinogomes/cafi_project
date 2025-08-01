from django.urls import path
from deliberasaun_cafi import views

urlpatterns = [
    path('', views.deliberasaun, name='deliberasaun'),
    path('add-deliberasaun', views.addDeliberasaun, name='add-deliberasaun'),
    path('detail-deliberasaun/<str:id>/', views.detailDeliberasaun, name='detail-deliberasaun'),
    path('edit-deliberasaun/<str:id>/', views.editDeliberasaun, name='edit-deliberasaun'),
    path('delete-deliberasaun/<str:id>/', views.deleteDeliberasaun, name='delete-deliberasaun'),
]