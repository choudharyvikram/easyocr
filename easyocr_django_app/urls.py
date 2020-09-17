from django.urls import path

from .views import ocr

urlpatterns = [
    path('ocr/',ocr, name='ocr')
]