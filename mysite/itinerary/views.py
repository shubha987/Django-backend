import json
from amadeus import Client, ResponseError, Location
from django.shortcuts import render,redirect
from django.contrib import messages
from .flight import Flight
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from .forms import UserRegisterForm
from django.contrib.auth import login, logout
from .hotel import Hotel
from .room import Room
from .metrics import Metrics
from dotenv import load_dotenv
import google.generativeai as genai
import requests
import os
load_dotenv()  ##loading all the environment variable

amadeus = Client()

# User registration view
def register(request):
    """
    Handles user registration. Displays a registration form, 
    processes it upon submission, and saves a new user if the form is valid.
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page.
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

# User login view
def loginpage(request):
    """
    Handles user login. Displays a login form, processes it upon submission, 
    and logs in the user if the form is valid.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')  # Redirect to the home page after successful login.
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Flight offers view
@login_required(login_url='login')
def flight_offers(request):
    """
    Handles flight search requests. Collects search parameters from the user, 
    retrieves flight offers and price metrics from Amadeus API, 
    and displays the results.
    """
    origin = request.POST.get('Origin')
    destination = request.POST.get('Destination')
    departure_date = request.POST.get('Departuredate')
    return_date = request.POST.get('Returndate')

    kwargs = {'originLocationCode': origin,
              'destinationLocationCode': destination,
              'departureDate': departure_date,
              'adults': 1
              }

    kwargs_metrics = {'originIataCode': origin,
                      'destinationIataCode': destination,
                      'departureDate': departure_date
                      }
    trip_purpose = ''
    try:
        if return_date:
            kwargs['returnDate'] = return_date
            kwargs_trip_purpose = {'originLocationCode': origin,
                                   'destinationLocationCode': destination,
                                   'departureDate': departure_date,
                                   'returnDate': return_date
                                   }

            trip_purpose = get_trip_purpose(**kwargs_trip_purpose)
        else:
            kwargs_metrics['oneWay'] = 'true'

        if origin and destination and departure_date:
            flight_offers = get_flight_offers(**kwargs)
            metrics = get_flight_price_metrics(**kwargs_metrics)
            cheapest_flight = get_cheapest_flight_price(flight_offers)
            is_good_deal = ''
            if metrics is not None:
                is_good_deal = rank_cheapest_flight(cheapest_flight, metrics['first'], metrics['third'])
                is_cheapest_flight_out_of_range(cheapest_flight, metrics)

            return render(request, 'results.html', {'flight_offers': flight_offers,
                                                                 'origin': origin,
                                                                 'destination': destination,
                                                                 'departure_date': departure_date,
                                                                 'return_date': return_date,
                                                                 'trip_purpose': trip_purpose,
                                                                 'metrics': metrics,
                                                                 'cheapest_flight': cheapest_flight,
                                                                 'is_good_deal': is_good_deal
                                                                })
    except ResponseError as error:
        messages.add_message(request, messages.ERROR, error.response.result['errors'][0]['detail'])
        return render(request, 'home.html', {})
    return render(request, 'home.html', {})


# Helper functions for flight offers
def get_flight_offers(**kwargs):
    """
    Fetches flight offers based on the provided search parameters.
    """
    search_flights = amadeus.shopping.flight_offers_search.get(**kwargs)
    flight_offers = []
    for flight in search_flights.data:
        offer = Flight(flight).construct_flights()
        flight_offers.append(offer)
    return flight_offers


def get_flight_price_metrics(**kwargs_metrics):
    """
    Fetches flight price metrics based on the provided search parameters.
    """

    kwargs_metrics['currencyCode'] = 'USD'
    metrics = amadeus.analytics.itinerary_price_metrics.get(**kwargs_metrics)
    return Metrics(metrics.data).construct_metrics()


def get_trip_purpose(**kwargs_trip_purpose):
    """
    Predicts the purpose of a trip (business or leisure) based on the provided parameters.
    """
    trip_purpose = amadeus.travel.predictions.trip_purpose.get(**kwargs_trip_purpose).data
    return trip_purpose['result']


# Helper function to get the cheapest flight price from a list of flight offers
def get_cheapest_flight_price(flight_offers):
    """
    Retrieves the price of the cheapest flight from the flight offers.
    """
    return flight_offers[0]['price'] if flight_offers else None


def rank_cheapest_flight(cheapest_flight_price, first_price, third_price):
    """
    Ranks the cheapest flight as a good deal, high, or typical based on price metrics.
    """
    cheapest_flight_price_to_number = float(cheapest_flight_price)
    first_price_to_number = float(first_price)
    third_price_to_number = float(third_price)
    if cheapest_flight_price_to_number < first_price_to_number:
        return 'A GOOD DEAL'
    elif cheapest_flight_price_to_number > third_price_to_number:
        return 'HIGH'
    else:
        return 'TYPICAL'

def is_cheapest_flight_out_of_range(cheapest_flight_price, metrics):
    """
    Adjusts the min and max values in the metrics if the cheapest flight is outside the recorded range.
    """
    min_price = float(metrics['min'])
    max_price = float(metrics['max'])
    cheapest_flight_price_to_number = float(cheapest_flight_price)
    if cheapest_flight_price_to_number < min_price:
        metrics['min'] = cheapest_flight_price
    elif cheapest_flight_price_to_number > max_price:
        metrics['max'] = cheapest_flight_price

# Origin airport search view
def origin_airport_search(request):
    """
    Handles AJAX requests to search for origin airports based on user input.
    """
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        try:
            data = amadeus.reference_data.locations.get(keyword=request.GET.get('term', None),
                                                        subType=Location.ANY).data
        except ResponseError as error:
            messages.add_message(request, messages.ERROR, error.response.result['errors'][0]['detail'])
    return HttpResponse(get_city_airport_list(data), 'application/json')

# Destination airport search view
def destination_airport_search(request):
    """
    Handles AJAX requests to search for destination airports based on user input.
    """
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        try:
            data = amadeus.reference_data.locations.get(keyword=request.GET.get('term', None),
                                                        subType=Location.ANY).data
        except ResponseError as error:
            messages.add_message(request, messages.ERROR, error.response.result['errors'][0]['detail'])
    return HttpResponse(get_city_airport_list(data), 'application/json')


def get_city_airport_list(data):
    """
    Formats the city and airport search results for display.
    """
    result = []
    for i, val in enumerate(data):
        result.append(data[i]['iataCode'] + ', ' + data[i]['name'])
    result = list(dict.fromkeys(result))
    return json.dumps(result)

# User logout view
def logoutpage(request):
    logout(request)
    return redirect('login')

# Hotel search view
def hotel(request):
    """
    Handles hotel search requests. Collects search parameters from the user, 
    retrieves hotel offers from Amadeus API, and displays the results.
    """
    origin = request.POST.get('Origin')
    checkinDate = request.POST.get('Checkindate')
    checkoutDate = request.POST.get('Checkoutdate')

    kwargs = {'cityCode': request.POST.get('Origin'),
              'checkInDate': request.POST.get('Checkindate'),
              'checkOutDate': request.POST.get('Checkoutdate')}

    if origin and checkinDate and checkoutDate:
        try:
            # Hotel List
            hotel_list = amadeus.reference_data.locations.hotels.by_city.get(cityCode=origin)
        except ResponseError as error:
            messages.add_message(request, messages.ERROR, error.response.body)
            return render(request, 'hotel_booking_form.html', {})
        hotel_offers = []
        hotel_ids = []
        for i in hotel_list.data:
            hotel_ids.append(i['hotelId'])
        num_hotels = 40
        kwargs = {'hotelIds': hotel_ids[0:num_hotels],
            'checkInDate': request.POST.get('Checkindate'),
            'checkOutDate': request.POST.get('Checkoutdate')}
        try:
            # Hotel Search
            search_hotels = amadeus.shopping.hotel_offers_search.get(**kwargs)
        except ResponseError as error:
            messages.add_message(request, messages.ERROR, error.response.body)
            return render(request, 'hotel_booking_form.html', {})
        try:
            for hotel in search_hotels.data:
                offer = Hotel(hotel).construct_hotel()
                hotel_offers.append(offer)
                response = zip(hotel_offers, search_hotels.data)

            return render(request, 'result_hotel.html', {'response': response,
                                                         'origin': origin,
                                                         'departureDate': checkinDate,
                                                         'returnDate': checkoutDate,
                                                         })
        except UnboundLocalError:
            messages.add_message(request, messages.ERROR, 'No hotels found.')
            return render(request, 'hotel_booking_form.html', {})
    return render(request, 'hotel_booking_form.html', {})

# View for rooms per hotel
def rooms_per_hotel(request, hotel, departureDate, returnDate):
    """
    Handles hotel room booking. Processes the booking request and makes a booking using Amadeus API.
    """
    try:
        # Search for rooms in a given hotel
        rooms = amadeus.shopping.hotel_offers_search.get(hotelIds=hotel,
                                                           checkInDate=departureDate,
                                                           checkOutDate=returnDate).data
        hotel_rooms = Room(rooms).construct_room()
        return render(request, 'rooms_per_hotel.html', {'response': hotel_rooms,
                                                             'name': rooms[0]['hotel']['name'],
                                                             })
    except (TypeError, AttributeError, ResponseError, KeyError) as error:
        messages.add_message(request, messages.ERROR, error)
        return render(request, 'rooms_per_hotel.html', {})

# Book hotel view
def book_hotel(request, offer_id):
    try:
        # Confirm availability of a given offer
        offer_availability = amadeus.shopping.hotel_offer_search(offer_id).get()
        if offer_availability.status_code == 200:
            guests = [{'id': 1, 'name': {'title': 'MR', 'firstName': 'BOB', 'lastName': 'SMITH'},
                       'contact': {'phone': '+33679278416', 'email': 'bob.smith@email.com'}}]

            payments = {'id': 1, 'method': 'creditCard',
                        'card': {'vendorCode': 'VI', 'cardNumber': '4151289722471370', 'expiryDate': '2027-08'}}
            booking = amadeus.booking.hotel_bookings.post(offer_id, guests, payments).data
        else:
            return render(request, 'booking.html', {'response': 'The room is not available'})
    except ResponseError as error:
        messages.add_message(request, messages.ERROR, error.response.body)
        return render(request, 'booking.html', {})
    return render(request, 'booking.html', {'id': booking[0]['id'],
                                                 'providerConfirmationId': booking[0]['providerConfirmationId']
                                                 })

# City search view
def city_search(request):
    """
    Handles AJAX requests to search for cities based on user input.
    """
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
      data = None  # Initialize data before the try block
    try:
      data = amadeus.reference_data.locations.get(keyword=request.GET.get('term', None),
                                                subType=Location.ANY).data
    except ResponseError as error:
      messages.add_message(request, messages.ERROR, error.response.body)
    finally:
      return HttpResponse(get_city_list(data), 'application/json')

def get_city_list(data):
    """
    Formats the city search results for display.
    """
    result = []
    if data is not None:
        for i ,val in enumerate(data):
            result.append(data[i]['iataCode'] + ', ' + data[i]['name'])
    return result

## tour spot 
##configureing the gemini api key
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

##function to load gemini pro model and get responses
model = genai.GenerativeModel('gemini-pro')

def fetch_image(tour_spot_name):
    response = requests.get(f'https://api.unsplash.com/search/photos?query={tour_spot_name}&client_id={os.getenv("UNSPLASH_API_KEY")}')
    data = response.json()
  
    # Check if the response has results
    if data['results']:
        # Return the URL of the first image
        return data['results'][0]['urls']['small']

    return None

def get_gemini_response(prompt):
    response = model.generate_content(prompt)

    # Check if the response is valid
    if not response.candidates or not response.text:
        return []

    tour_spot_descriptions = response.text.split('* **')

    # Extract just the tour spot names from the descriptions
    tour_spots = []
    for desc in tour_spot_descriptions:
        tour_spot_name = desc.split('**')[0].strip()

        if tour_spot_name:
            image_url = fetch_image(tour_spot_name)
            if image_url:
                tour_spots.append((tour_spot_name, image_url))

        # Stop when we have 6 tour spots
        if len(tour_spots) == 6:
            break

    return tour_spots

def tour_spot(request):
    """
    Handles tour spot recommendations. Collects a place name from the user, 
    fetches tour spot recommendations using Gemini AI model, 
    and displays them along with images.
    """
    tour_spots = []
    if request.method == 'POST':
        place_name = request.POST['place']

        # Use Gemini API to generate a list of recommended tour spots
        tour_spots = get_gemini_response("Recommend tour spots in " + place_name)
        tour_spots = [(spot.replace(':', ''), image_url) for spot, image_url in tour_spots]

    return render(request, 'tour_spot.html', {'tour_spots': tour_spots})

#### for combination 
def get_hotel_offer(cityCode, checkInDate, checkOutDate):
    """
    Fetches hotel offers from Amadeus API based on the provided city code and dates.
    """
    try:
        # Fetch hotel list
        hotel_list = amadeus.reference_data.locations.hotels.by_city.get(cityCode=cityCode)
        hotel_ids = [hotel['hotelId'] for hotel in hotel_list.data]
        num_hotels = 40

        # Fetch hotel offers
        kwargs = {'hotelIds': hotel_ids[:num_hotels],
                  'checkInDate': checkInDate,
                  'checkOutDate': checkOutDate}
        search_hotels = amadeus.shopping.hotel_offers_search.get(**kwargs)

        # Construct hotel offers
        hotel_offers = [Hotel(hotel).construct_hotel() for hotel in search_hotels.data]

        return hotel_offers

    except ResponseError as error:
        print(f"An error occurred: {error.response.body}")
        return []


def get_city_from_airport_serach(term):
    """
    Fetches city from Amadeus API based on the provided airport code.
    """
    try:
        data = amadeus.reference_data.locations.get(keyword=term, subType=Location.ANY).data
        for i in data:
            if i['iataCode'] == term:
                return i['name']
    except ResponseError as error:
        print(f"An error occurred: {error.response.body}")
    return None

@login_required(login_url='login')
def search_all(request):
    """
    Handles flight search, hotel booking, and tour spot searching requests. 
    Collects search parameters from the user, retrieves data from Amadeus API, 
    and displays the results.
    """
    # Initialize empty values
    flight_offers, hotel_offers, tour_spots = [], [], []
    
    if request.method == 'POST':
        # Collect common parameters
        flight_origin = request.POST.get('flight_origin')
        flight_destination = request.POST.get('flight_destination')
        flight_departure_date = request.POST.get('flight_departure_date')
        flight_return_date = request.POST.get('flight_return_date')
        travel_type = request.POST.get('travel_type')  # Do you prefer traveling alone or with family?
        place_type = request.POST.get('place_type')  # Do you prefer modern cities or historical sites?
        activity = request.POST.get('activity')  # Do you prefer adventurous activities or relaxing experiences?


        hotel_city = flight_destination
        hotel_check_in_date = flight_departure_date
        hotel_check_out_date = flight_return_date

        tour_city =  get_city_from_airport_serach(flight_destination)
        # Validate and prepare flight parameters
        if flight_origin and flight_destination and flight_departure_date:
            flight_kwargs = {
                'originLocationCode': flight_origin,
                'destinationLocationCode': flight_destination,
                'departureDate': flight_departure_date,
                'adults': 1
            }
            if flight_return_date:
                flight_kwargs['returnDate'] = flight_return_date

            try:
                flight_offers = get_flight_offers(**flight_kwargs)
                flight_offers = sorted(flight_offers, key=lambda offer: offer['price'])[:5]
            except ResponseError as error:
                messages.add_message(request, messages.ERROR, "Error fetching flight offers.")
            except Exception as e:
                messages.add_message(request, messages.ERROR, "Unexpected error occurred while fetching flight offers.")

        # Validate and prepare hotel parameters
        if hotel_city and hotel_check_in_date and hotel_check_out_date:
            try:
                hotel_offers = get_hotel_offer(hotel_city, hotel_check_in_date, hotel_check_out_date)
                hotel_offers = sorted(hotel_offers, key=lambda offer: offer['price'])[:5]
            except ResponseError as error:
                messages.add_message(request, messages.ERROR, "Error fetching hotel offers.")
            except Exception as e:
                messages.add_message(request, messages.ERROR, "Unexpected error occurred while fetching hotel offers.")

        if tour_city:
            try:
                query = f"Recommend {place_type} {activity} spots in {tour_city} for {travel_type} travel"
                tour_spots = get_gemini_response(query)
                tour_spots = [(spot.replace(':', ''), image_url) for spot, image_url in tour_spots]
            except Exception as e:
              messages.add_message(request, messages.ERROR, f"Error fetching tour spots: {str(e)}")

        # Render the itinerary_result.html template with the search results
        return render(request, 'itinerary_result.html', {
            'flight_offers': flight_offers,
            'hotel_offers': hotel_offers,
            'tour_spots': tour_spots,
        })

    # Render the itinerary.html template for GET requests
    return render(request, 'itinerary.html')