# notas/urls.py

from django.urls import path
from . import views

app_name = 'notas'

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastrar/', views.cadastrar_nota, name='cadastrar'),
    path('detalhe/<int:id>/', views.detalhe_nota, name='detalhe'),
]
