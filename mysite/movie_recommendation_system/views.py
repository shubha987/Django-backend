from django.shortcuts import render
import requests
import os
from dotenv import load_dotenv
import google.generativeai as genai
import re
load_dotenv()  ##loading all the environment variable

##configureing the gemini api key
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

##function to load gemini pro model and get responses
model = genai.GenerativeModel('gemini-pro')

def get_gemini_response(prompt):
    response = model.generate_content(prompt)

# Check if the response is valid
    if not response.candidates or not response.text:
        return []

    movie_descriptions = response.text.split('* **')

    # Extract just the movie names from the descriptions
    movie_names = []
    for desc in movie_descriptions:
        movie_name = desc.split('**')[0].strip()

        # Remove the year from the movie name
        movie_name = re.sub(r'\s*\(\d{4}\)\s*$', '', movie_name)

        if movie_name and fetch_poster(movie_name):
            movie_names.append(movie_name)

        # Stop when we have 6 movies
        if len(movie_names) == 6:
            break

    return movie_names

def fetch_poster(movie_name):
    response = requests.get('http://www.omdbapi.com/?t={}&apikey=e8f2d945'.format(movie_name))
    if response.status_code == 200:
        data = response.json()
        if 'Poster' in data and data['Poster'] != 'N/A':
            return data['Poster']
    return None

def home(request):
    return render(request, 'enter_movie.html')

def recommend_movies(request):
    if request.method == 'POST':
        movie_name = request.POST['movie_name']

        # Use Gemini API to generate a list of recommended movies
        recommended_movies = get_gemini_response("Recommend movies similar to " + movie_name)

        # Fetch the posters for the recommended movies
        posters = [fetch_poster(movie.strip()) for movie in recommended_movies]

        return render(request, 'recommend.html', {'movie_data': zip(recommended_movies, posters)})

    return render(request, 'enter_movie.html')