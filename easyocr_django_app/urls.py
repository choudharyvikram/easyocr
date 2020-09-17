from django.urls import path

from .views import ocr

urlpatterns = [
    path('',ocr, name='ocr')
]