from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.conf import settings
from datetime import datetime
import os
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
        data_hora_envio = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        return JsonResponse({'data_hora_envio': data_hora_envio})

    return render(request, 'send_file.html')
