# Architecture

The architecture of the MySite Django-Project consists of three main components: the IrisApp,the Movie Recommendation System and a welcome deck.

## mysite 
This Django project,<code>mysite</code>, is a web application that integrates multiple smaller applications, including <code>book_recommender</code> and <code>irisapp</code>. Here's a high-level overview of the project's architecture:

<ol>
 <li>ASGI Configuration (<code>asgi.py</code>): This file configures the ASGI server for the Django project. It sets the environment variable <code>DJANGO_SETTINGS_MODULE</code> to point to the settings file of the project and creates an instance of the ASGI application.</li>

 <li>WSGI Configuration (<code>wsgi.py</code>): This file configures the WSGI server for the Django project. It sets the environment variable <code>DJANGO_SETTINGS_MODULE</code> to point to the settings file of the project and creates an instance of the WSGI application.</li>

 <li>URL Configuration (<code>urls.py</code>): This file maps URLs to view functions. It includes the URL configurations of the <code>welcome_deck</code>,<code>book_recommender</code>, and <code>irisapp</code> applications.</li>

<li>Settings (<code>settings.py</code>): This file contains the settings for the Django project. It specifies the installed applications, middleware, database configuration, password validators, internationalization settings, static files settings, and other settings.</li>
</ol>

## IrisApp

This Django-application under django project `mysite` appears to be a simple web application for predicting the species of an Iris flower based on its sepal and petal dimensions. Here's a high-level overview of the project's architecture:
<ol>
 <li>Models (<code>models.py</code>): The Iris model is defined here. It represents an Iris flower with fields for sepal length, sepal width, petal length, petal width, and species. This model is used to store Iris instances in the database.</li>

 <li>Views (<code>views.py</code>): This file contains the predictor view function. This function handles HTTP requests to the application. If the request method is <code>POST</code>, it retrieves the form data, uses a pre-trained model to predict the <code>Iris</code> species, and renders a template(<code>mysite/templates/main.html</code>) with the prediction result. If the request method is not POST, it simply renders a template (<code>mysite/templates/main.html</code>).</li>

 <li>URLs (<code>urls.py</code>): This file maps URLs to view functions. In this case, it maps the root URL <code>('')</code> to the predictor view function.</li>

 <li>Admin (<code>admin.py</code>): This file configures the Django admin site. It registers the Iris model with the admin site and specifies which fields to display and search by.</li>

 <li>Apps (<code>apps.py</code>): This file contains the IrisappConfig class, which is a configuration class for the irisapp application. It specifies the default auto field and the name of the application.</li>

 <li>Machine Learning Model (<code>irismodel.joblib</code>): This is a pre-trained machine learning model for predicting the species of an Iris flower. It's loaded in views.py and used to make predictions.Main dynamic model is present in <code>mysite/savedmodels/irismodel.joblib</code></li>

 <li>Tests:
     <ul>
     <li>Model Tests (<code>test_models.py</code>) : These tests check the creation of <code>Iris</code>instances and their attributes.</li>
     <li>View Tests (<code>test_models.py</code>) : These tests check the <code>predictor</code> view function. They send a POST request with sample data and check the response status code and the prediction result.</li>
     <li>URL Tests (<code>test_models.py</code>) :  These tests check if the URL for the <code>predictor</code> view function resolves correctly..</li>
     </ul>
 </li>

 <li>Migrations (<code>0001_initial.py</code>): This file is a migration that Django uses to create the Iris model in the database. It specifies the fields of the Iris model and their types.</li>
 </ol>

The flow of the application is as follows:

<ul>
<li>A user submits a form with the dimensions of an Iris flower.</li>
<li>The predictor view retrieves the form data and uses the pre-trained model to predict the Iris species.</li>
<li>The prediction result is passed to a template and rendered as a response to the user.</li>
<li>The tests ensure that the models, views, and URLs are working as expected.</li>
<li>The migration file <code>0001_initial.py</code> is used to create the Iris model in the database.</li>
</ul>


## Movie Recommendation System

This Django application appears to be a simple web application for recommending popular books. Here's a high-level overview of the project's architecture:

<ol>
<li>Views (<code>views.py</code>): This file defines the views for your application. It includes two views:<code>home</code> and <code>recommend_movies</code>. The home view simply renders the <code>'index.html'</code> template. The <code>recommend_movies </code>view takes a POST request with a movie name, uses the Gemini API to generate a list of recommended movies, fetches the posters for these movies, and then renders the 'recommend.html' template with this data.</li>

<li>URLs (<code>urls.py</code>): This file defines the URL routes for your application. It includes two routes: the root route <code>('')</code>, which maps to the <code>home</code> view, and the <code>'recommend/'</code> route, which maps to the <code>recommend_movies</code>view.</li>

<li>Apps (<code>apps.py</code>): This file contains he configuration for your Django application. It defines a <code>MovieRecommendationSystemConfig</code>class that sets the name of the application.</li>

<li>Admin (<code>admin.py</code>): This file is used to define the admin site configuration for the book_recommender application. However, it's currently empty and doesn't register any models.</li>

<li>Models(<code>models.py</code>): There are no models defined in your application, as it doesn't interact with a database. All data is fetched in real-time from the Gemini API and the OMDB API.</li>

<li>APIs: Your application uses two APIs: the <code>Gemini AP</code>I to generate movie recommendations, and the <code>OMDB API</code> to fetch movie posters.</li>

</ol>

Here's a diagram that represents the architecture of your application:

```bash
User
  |
  | --(Enter movie name)--> Home View --(Render 'index.html')--> User
  |
  | --(Submit movie name)--> Recommend Movies View --(Gemini API)--> Movie Recommendations
  |                                                         |
  |                                                         | --(OMDB API)--> Movie Posters
  |                                                         |
  | --(Render 'recommend.html' with movie recommendations and posters)--> User
```

## Integration

To integrate <code>mysite</code> with <code>irisapp</code> and <code>book_recommender</code>, you would need to modify the <code>urls.py</code> and <code>settings.py</code> files in the mysite project.

<ol>
 <li>Update <code>settings.py</code>:
     <ul>
        <li>Add <code>irisapp</code> and <code>book_recommender</code> to the <code>INSTALLED_APPS</code> list. This will let Django know that these apps are part of the project.</li>
     </ul>
 </li>

```bash
# settings.py
INSTALLED_APPS = [
    # other apps...
    'irisapp',
    'movie_recommendation_system',
]
```
<li>Update <code>urls.py</code>:
     <ul>
        <li>Include the URLs of<code>irisapp</code> and <code>book_recommender</code> n the project's URL configuration. This will map the URLs of these apps to their respective view functions.</li>
     </ul>
 </li>

 ```bash
# urls.py
from django.urls import include, path

urlpatterns = [
    # other paths...
    path('iris/', include('irisapp.urls')),
    path('book/', include('book_recommender.urls')),
]
```
With these changes, when a user visits <code>yourwebsite.com/iris</code>, they will be directed to the irisapp application, and when they visit <code>yourwebsite.com/book</code>, they will be directed to the book_recommender application.


## Machine Learning Models

<ol>
<li>Irisapp (<code>irismodel.joblib</code>): The saved model is in the <code>mysite/savedmodels/irismodel.joblib</code> and created in the <code>venv(python3.11.5)</code>. It used  the scikit-learn library to create a Random Forest Classifier for the Iris dataset. 
<ol>
 <li>Loading the iris datset:</li>

 ```bash
from sklearn.datasets import load_iris
data = load_iris()
```
The <code>load_iris</code> function from scikit-learn's datasets module is used to load the Iris dataset. This dataset is stored in the <code>data</code> variable.

 <li>Creating a pandas DataFrame and Series from the Iris dataset</li>

```bash
import pandas as pd
X_data = pd.DataFrame(data.data, columns = data.feature_names)
y_data = pd.Series(data = data.target, name = 'Targets')
```
The features of the Iris dataset (sepal length, sepal width, petal length, and petal width) are stored in a pandas DataFrame X_data, and the target variable (the species of the Iris) is stored in a pandas Series <code>y_data</code>.

 <li>Splitting the data into training and testing sets:</li>

```bash
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size = 0.2)
```
The <code>train_test_split</code> function from scikit-learn is used to split the dataset into a training set and a testing set. 80% of the data is used for training the model, and 20% is used for testing the model.

<li>Creating a Random Forest Classifier:</li>

```bash
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
```
A Random Forest Classifier is created using the <code>RandomForestClassifier</code> class from scikit-learn's ensemble module. This classifier is stored in the <code>model</code> variable.

 <li>Fitting the model to the training data:<li>

```bash
model.fit(X_train, y_train)
```
The <code>fit</code> method of the Random Forest Classifier is used to train the model on the training data.

 <li>Making predictions on the testing data:</li>

```bash
y_pred = model.predict(X_test)
```
The <code>predict</code> method of the Random Forest Classifier is used to make predictions on the testing data. These predictions are stored in the <code>y_pred</code> variable.

 <li>Calculating the accuracy of the model:</li>

```bash
from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_pred)
```
The <code>accuracy_score</code> function from scikit-learn's metrics module is used to calculate the accuracy of the model. This is done by comparing the model's predictions on the testing data (<code>y_pred</code>) with the actual species of the Iris flowers in the testing data (<code>y_test</code>).

 <li>Saving the model:</li>

```bash
from joblib import dump
dump(model, './../savedmodels/irismodel.joblib')
```
The <code>dump</code>function from the joblib module is used to save the trained model to a file. This allows the model to be loaded later without needing to be retrained.

The accuracy of <code>0.9</code> indicates that the model correctly predicted the species of the Iris flower <code>90%</code> of the time on the testing data.
</ol>


## Itinerary 
The Itinerary app is designed to help users plan their travel itineraries by providing recommendations for flights, hotels, and tourist spots. Here's a high-level overview of the project's architecture:

```bash
mysite/
│
├── mysite/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── itinerary/
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── flight.py
│   ├── forms.py
│   ├── hotel.py
│   ├── metrics.py 
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └──views.py
│   
│    
│
└── manage.py
```

## Components:

- **`itinerary/`**: This directory contains the Django application code.
  - **`migrations/`**: Contains Django database migration files.
  - **`templates/`**: Contains HTML templates used for rendering views.
  - **`__init__.py`**: Initializes the Python package.
  - **`admin.py`**: Configuration for Django admin interface.
  - **`apps.py`**: Configuration for the Django application.
  - **`flight.py`**: Defines classes and functions for handling flight-related operations.
  - **`forms.py`**: Defines Django forms for user input validation.
  - **`hotel.py`**: Defines classes and functions for handling hotel-related operations.
  - **`room.py`**: The `Room` class defines methods for handling hotel-related operations and extracting room information from data retrieved from Amadeus API.
  - **`metrics.py`**: Defines classes and functions for handling flight price metrics.
  - **`tests.py`**: Contains unit tests for the application.
  - **`urls.py`**: URL configuration for mapping views to URLs.
  - **`views.py`**: Contains controller logic for handling HTTP requests.

- **`.env`**: Configuration file for environment variables.

- **`manage.py`**: Django management script for various tasks.

- **`requirements.txt`**: File listing Python dependencies required for the project.

## Views:

### `register(request)`
- **Description**: Handles user registration.
- **Method**: `POST`
- **Form Submitted**: User registration form
- **Validates**: Form data
- **Saves**: New user if form is valid
- **Redirects to**: Login page
- **Template**: `register.html`

### `loginpage(request)`
- **Description**: Handles user login.
- **Method**: `POST`
- **Form Submitted**: Login form
- **Validates**: Form data
- **Logs in**: User if form is valid
- **Redirects to**: Home page
- **Template**: `login.html`

### `flight_offers(request)`
- **Description**: Handles flight search requests.
- **Method**: `GET` and `POST`
- **Parameters**: Origin, Destination, Departure Date, Return Date (optional)
- **Collects**: Search parameters from the user
- **Retrieves**: Flight offers and price metrics from Amadeus API
- **Displays**: Search results
- **Template**: `results.html`
- **Dependencies**: `amadeus` client, `Flight` class, `Metrics` class

### `origin_airport_search(request)`
- **Description**: Handles AJAX requests to search for origin airports based on user input.
- **Method**: `GET`
- **Parameters**: `term` (optional)
- **Retrieves**: Origin airports matching the search term
- **Returns**: JSON list of matching airports
- **Dependencies**: `amadeus` client

### `destination_airport_search(request)`
- **Description**: Handles AJAX requests to search for destination airports based on user input.
- **Method**: `GET`
- **Parameters**: `term` (optional)
- **Retrieves**: Destination airports matching the search term
- **Returns**: JSON list of matching airports
- **Dependencies**: `amadeus` client

### `logoutpage(request)`
- **Description**: Logs out the user.
- **Method**: `GET`
- **Logs out**: Currently logged-in user
- **Redirects to**: Login page

### `hotel(request)`
- **Description**: Handles hotel search requests.
- **Method**: `POST`
- **Parameters**: Origin, Check-in Date, Checkout Date
- **Collects**: Search parameters from the user
- **Retrieves**: Hotel offers from Amadeus API
- **Displays**: Search results
- **Template**: `result_hotel.html`
- **Dependencies**: `amadeus` client, `Hotel` class

### `rooms_per_hotel(request, hotel, departureDate, returnDate)`
- **Description**: Handles hotel room booking.
- **Method**: `GET`
- **Parameters**: Hotel ID, Departure Date, Return Date
- **Retrieves**: Rooms available in a given hotel
- **Displays**: Room options
- **Template**: `rooms_per_hotel.html`
- **Dependencies**: `amadeus` client, `Room` class

### `book_hotel(request, offer_id)`
- **Description**: Books a hotel room.
- **Method**: `GET`
- **Parameters**: Offer ID
- **Confirms**: Availability of the room
- **Books**: Room if available
- **Displays**: Booking details
- **Template**: `booking.html`
- **Dependencies**: `amadeus` client

### `city_search(request)`
- **Description**: Handles AJAX requests to search for cities based on user input.
- **Method**: `GET`
- **Parameters**: `term` (optional)
- **Retrieves**: Cities matching the search term
- **Returns**: JSON list of matching cities
- **Dependencies**: `amadeus` client

### `tour_spot(request)`
- **Description**: Handles tour spot recommendations.
- **Method**: `POST`
- **Parameters**: Place name
- **Generates**: Tour spot recommendations using Gemini AI model
- **Displays**: Tour spots along with images
- **Template**: `tour_spot.html`
- **Dependencies**: `requests`, `genai`, `os`

## Flight Class and Associated Functions:

### Flight Class:

- **Purpose**: The `Flight` class is responsible for constructing flight offers from the flight data retrieved from an external API.
- **Attributes**:
  - `flight`: Represents the flight data obtained from the external API.
- **Methods**:
  - `construct_flights(self)`: Constructs flight offers from the flight data.
    - **Parameters**: None
    - **Returns**: A dictionary containing flight offer details.
    - **Details**:
      - Parses the flight data and extracts information such as price, flight ID, departure airport, arrival airport, departure date, arrival date, airline logo, airline code, and flight duration.
      - Handles both one-stop and direct flights, extracting relevant details for each.
      - Utilizes helper functions `get_airline_logo()`, `get_hour()`, and `get_stoptime()` to format and extract specific information.

### Helper Functions:

1. **`get_airline_logo(carrier_code)`**:
   - **Purpose**: Returns the URL of the airline logo based on the carrier code.
   - **Parameters**:
     - `carrier_code`: Code representing the airline carrier.
   - **Returns**: URL of the airline logo.
   
2. **`get_hour(date_time)`**:
   - **Purpose**: Formats the date and time in '%H:%M' format.
   - **Parameters**:
     - `date_time`: Date and time in string format.
   - **Returns**: Formatted date and time.
   
3. **`get_stoptime(total_duration, first_flight_duration, second_flight_duration)`**:
   - **Purpose**: Calculates the stop time between two flights for one-stop flights.
   - **Parameters**:
     - `total_duration`: Total duration of the flight.
     - `first_flight_duration`: Duration of the first flight segment.
     - `second_flight_duration`: Duration of the second flight segment.
   - **Returns**: Stop time between the flights.

### Usage:

- The `Flight` class and its associated functions are utilized within the Django application for processing flight search results obtained from the Amadeus API.
- These functions parse the raw flight data, extract relevant details, and format them into structured flight offers, which are then displayed to the users on the website.


### Metrics Class:

- **Purpose**: The `Metrics` class is responsible for constructing flight price metrics from the data retrieved from an external API.
- **Attributes**:
  - `metric`: Represents the metric data obtained from the external API.
- **Methods**:
  - `construct_metrics(self)`: Constructs flight price metrics from the metric data.
    - **Parameters**: None
    - **Returns**: A dictionary containing flight price metrics.
    - **Details**:
      - Tries to extract minimum, first quartile, median, third quartile, and maximum price metrics from the metric data.
      - Handles potential errors such as IndexError, TypeError, AttributeError, and KeyError gracefully.
      - If the extraction is successful, returns a dictionary containing the extracted metrics. Otherwise, returns `None`.

### Usage:

- The `Metrics` class is utilized within the Django application for processing flight price metrics obtained from the Amadeus API.
- These metrics provide insights into the distribution of flight prices, allowing users to make informed decisions when selecting flights.
- The class helps in extracting and formatting these metrics for display to users on the website.

### Hotel Class:

- **Purpose**: The `Hotel` class defines methods for processing hotel information retrieved from an external API.
- **Attributes**:
  - `hotel`: Represents the hotel data obtained from the external API.
- **Methods**:
  - `construct_hotel(self)`: Constructs hotel details from the hotel data.
    - **Parameters**: None
    - **Returns**: A dictionary containing hotel information.
    - **Details**:
      - Tries to extract relevant information such as price, name, hotel ID, and address from the hotel data.
      - Utilizes the `geocoder` library to retrieve the address based on latitude and longitude coordinates.
      - Handles potential errors such as TypeError, AttributeError, and KeyError gracefully.
      - If the extraction is successful, returns a dictionary containing the constructed hotel details. Otherwise, returns `None`.

### Usage:

- The `Hotel` class is used within the Django application for processing hotel information obtained from the Amadeus API.
- It facilitates the extraction and formatting of hotel details such as price, name, and address for display to users on the website.
- The class plays a crucial role in enabling users to view available hotel options and make informed decisions based on their preferences.

### Room Class:

- **Purpose**: The `Room` class defines methods for handling hotel-related operations and extracting room information from data retrieved from an external API.
- **Attributes**:
  - `rooms`: Represents the room data obtained from the external API.
- **Methods**:
  - `construct_room(self)`: Constructs hotel room information from the room data.
    - **Parameters**: None
    - **Returns**: A list of dictionaries containing hotel room details.
    - **Details**:
      - Tries to iterate through the room data and extract relevant information such as price, description, and offer ID for each room.
      - Handles potential errors such as TypeError, AttributeError, and KeyError gracefully.
      - If the extraction is successful, returns a list of dictionaries containing the extracted room details. Otherwise, returns an empty list.

### Usage:

- The `Room` class is utilized within the Django application for processing hotel room information obtained from the Amadeus API.
- It assists in extracting and formatting hotel room details for display to users on the website.
- The class plays a crucial role in enabling users to browse and select hotel rooms based on their preferences and budget.
