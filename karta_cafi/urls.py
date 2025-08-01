from django.urls import path
from karta_cafi import views

urlpatterns = [
    # karta tama
    path('karta-tama/', views.kartaTama, name='karta-tama'),
    path('add-karta-tama/', views.addKTama, name='add-karta-tama'),
    path('detail-karta-tama/<int:id>/', views.detailkt, name='detail-karta-tama'),
    path('edit-karta-tama/<int:id>/', views.editkt, name='edit-karta-tama'),
    path('delete-karta-tama/<int:id>/', views.deletekt, name='delete-karta-tama'),
    # karta sai
    path('karta-sai/', views.kartasai, name='karta-sai'),
    path('add-karta-sai/', views.addks, name='add-karta-sai'),
    path('detail-karta-sai/<int:id>/', views.detailks, name='detail-karta-sai'),
    path('edit-karta-sai/<int:id>/', views.editks, name='edit-karta-sai'),
    path('delete-karta-sai/<int:id>/', views.deleteks, name='delete-karta-sai'),
]