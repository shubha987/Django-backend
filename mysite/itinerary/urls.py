from django.urls import path

from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
    path('dept/', views.flight_offers, name='home'),
    path('origin_airport_search/', views.origin_airport_search, name='origin_airport_search'),
    path('destination_airport_search/', views.destination_airport_search, name='destination_airport_search'),
    path('hotel/', views.hotel, name='demo_form'),
    path('city_search/', views.city_search, name='city_search'),
    path('book_hotel/<str:offer_id>', views.book_hotel, name='book_hotel'),
    path('rooms_per_hotel/<str:hotel>/<str:departureDate>/<str:returnDate>', views.rooms_per_hotel, name='rooms_per_hotel'),
    path('tour_spot/', views.tour_spot, name='tour_spot'),
    path('itinerary/', views.search_all, name='itinerary'),
]