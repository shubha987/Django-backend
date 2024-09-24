from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('bitcoin-news/',views.get_bitcoin_news, name='get_bitcoin_news'),
    path('upload/', views.upload_news, name='upload_news'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
