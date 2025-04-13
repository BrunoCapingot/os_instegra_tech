from django.shortcuts import render
from django.views.generic import TemplateView, ListView

class HomeView(TemplateView):
    template_name = 'index.html'

class IdentificadoresView(TemplateView):
    template_name = 'identificadores_y_m.html'

class CamerasView(TemplateView):
    template_name = 'sistema_de_cameras.html'

class FramesView(TemplateView):
    template_name = 'gravar_frames.html'