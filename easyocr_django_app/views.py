from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

import time
import os
import cv2

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
        filename = f'media/{filename}'
        # print('*************************', media_path+filename)
        image, text = ocr_image(filename)
        cv2.imwrite(f'media/{timestamp}/{timestamp}_OCRed.jpg',image)
        with open(f'media/{timestamp}/{timestamp}_output.txt','w') as f:
            f.write(text)

        return render(request, 'index.html',{'image_path':f'media/{timestamp}/{timestamp}_OCRed.jpg',
                                            'text':text})
    return render(request, 'index.html')