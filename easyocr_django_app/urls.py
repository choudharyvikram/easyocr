from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import ocr

urlpatterns = [
    path('ocr/',ocr, name='ocr')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
