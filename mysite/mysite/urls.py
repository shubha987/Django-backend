
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/',include('welcome_deck.urls')),
    path('movie/',include('movie_recommendation_system.urls')),
    path('iris/',include('irisapp.urls')),
    path('flight/',include('itinerary.urls')), 
    path('',views.index,name='index'),
    #path('video/',include('videoconferenceapp.urls')),
    path('videocall/',include('videoconference.urls')),
    path('matchmaking/',include('matchmaking.urls')),
     path('api/', include('newsapp.urls')),
] 
