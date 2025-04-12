from django.shortcuts import render
import base64
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import cv2
import numpy as np
import json

def index(request):
    return render(request, 'index.html')

def identificadores_view(request):
    return render(request, 'identificadores_y_m.html')

def sistema_de_cameras(request):
    return render(request, 'sistema_de_cameras.html')

def gravar_frames(request):
    return render(request, 'gravar_frames.html')