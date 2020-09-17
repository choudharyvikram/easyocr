from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

import time
import os

from .easy_ocr import ocr_image
from easyocr_django.settings import BASE_DIR

media_path = BASE_DIR + '/media/'


def ocr(request):
    if request.method == 'POST':
        image = request.FILES.get('imagefile', None)
        timestamp = str(int(time.time()*100000))
        os.mkdir(f'media/{timestamp}')
        fileSystemStorageObject = FileSystemStorage()
        filename = fileSystemStorageObject.save(f'{timestamp}/{timestamp}_{image.name}',image)
        print('*************************', filename)
        return render(request, 'index.html')
    return render(request, 'index.html')