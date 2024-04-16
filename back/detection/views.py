from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.conf import settings
from datetime import datetime
import os

from imageai.Detection.Custom import CustomObjectDetection


# Create your views here.


def detection(request):
    print('detection')
    return HttpResponse('DETECTION ALIVE')


def detect(request):
    print('DETECT ALIVE')

    if request.method == 'POST' and request.FILES:
        uploaded_file = request.FILES['picture']

        # Salvar o arquivo em algum lugar ou faça o que você precisa com ele.
        save_path = os.path.join(settings.MEDIA_ROOT,
                                 uploaded_file.name)  # caminho onde sera salvo, definido no arquivo settings.py

        with open(save_path, 'wb') as destination:  # salva o arquivo recebido no diretorio
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        # Obtendo a data e hora atual
        receiveDate= datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(uploaded_file)

        imageAnalysis = run_detection(save_path)

        return JsonResponse({'receiveDate': receiveDate, 'imageAnalysis': imageAnalysis}, safe=False)

    return render(request, 'send_file.html')

def run_detection(image):
    detector = CustomObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath('detection/models/yolov3_tuta.pt')
    detector.setJsonPath('detection/json/tuta_yolov3_detection_config.json')
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image= image, output_image_path="detection/media/analysis/img1-detected.jpg")

    # for detection in detections:
    #     print(detections)
    #     print('---------------------------')
    #     print(detection)
    return detections

