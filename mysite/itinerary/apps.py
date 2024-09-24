from django.apps import AppConfig


class ItineraryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'itinerary'

class FlightPriceConfig(AppConfig):
    name = 'flight_price'