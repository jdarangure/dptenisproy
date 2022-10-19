from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('registradist/', views.registraDist),
    path('editardist/<_id_dist>', views.editarDist),
    path('editdist/', views.editDist),
    path('borradist/<_id_dist>', views.borraDist),
]