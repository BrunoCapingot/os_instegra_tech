from django.urls import path
from . import views

app_name = 'id'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('identificacao/', views.IdentificadoresView.as_view(), name='identificacao'),
    path('sistema_de_cameras/', views.CamerasView.as_view(), name='sistema_de_cameras'),
    path('gravar_frames/', views.FramesView.as_view(), name='gravar_frames'),
]
