from django.http import HttpResponse

from .models import Item
from django.views.decorators.csrf import csrf_exempt
import base64
import numpy as np
import json
from django.shortcuts import render
import tempfile
import cv2
from ultralytics import YOLO


def index(request):
    return render(request, 'index.html')

def identificadores_view(request):
    return render(request, 'identificadores_y_m.html')

def sistema_de_cameras(request):
    return render(request, 'sistema_de_cameras.html')

def upload_video(request):
    list_class_name:list = list()
    if request.method == 'POST' and request.FILES.get('video'):
        video_file = request.FILES['video']
        with tempfile.NamedTemporaryFile(suffix='.mp4', delete=True) as temp_video:
            for chunk in video_file.chunks():
                temp_video.write(chunk)
            temp_video.flush()

            cap = cv2.VideoCapture(temp_video.name)
            model = YOLO(r'C:\Users\CPGT\PycharmProjects\IA\IdentificadoresYM\datasets\Modelos\yolo11n.pt')
            frame_count = 0
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                results = model(frame)
                classes = results[0].boxes.cls.cpu().numpy()
                for classe in classes:
                    class_name = model.names[int(classe)]
                    if class_name not in list_class_name:
                        list_class_name.append(class_name)
                results[0].boxes = results[0].boxes[results[0].boxes.conf >= 0.6]
                #annotated_frame = results[0].plot()
                #cv2.imshow("Detecção de Objetos", annotated_frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):  # Pressione Q para sair
                    break
                frame_count += 1
            #cap.release()
            #cv2.destroyAllWindows()
        return render(request, 'lista_de_classes_identificadas.html', {'list_class_name': list_class_name})
        print(list_class_name)

    return render(request, 'sistema_de_identificacao_por_gravacao.html')


@csrf_exempt
def gravar_frames(request):
    if request.method == 'POST':
            data = json.loads(request.body.decode('utf-8'))
            imagem_base64 = data.get('imagem')
            imagem_base64 = imagem_base64.split(',')[1]
            imagem_bytes = base64.b64decode(imagem_base64)
            np_arr = np.frombuffer(imagem_bytes, np.uint8)
            frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
            model = YOLO(r"C:\Users\CPGT\PycharmProjects\IA\IdentificadoresYM\runs\detect\150_3_itens\weights\best.pt")
            results = model(frame)
            results[0].boxes = results[0].boxes[results[0].boxes.conf >= 0.6]
            annotated_frame = results[0].plot()

    return render(request, 'gravar_frames.html')

def lista_de_classes(request):
    pass


def resultado_identificacao(request):
    itens = Item.objects.all()
    print(itens)
    return render(request, 'resultado_identificacao.html',{'itens': itens})