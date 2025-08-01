from django.urls import path
from ata_reuniaun import views

urlpatterns = [
    path('', views.ata, name='ata'),
    path('add-ata/', views.addAta, name='add-ata'),
    path('detail-ata/<str:id>/', views.detailAta, name='detail-ata'),
    path('edit-ata/<str:id>/', views.editAta, name='edit-ata'),
    path('delete-ata/<str:id>/', views.deleteAta, name='delete-ata'),
]