from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse
import os
from dotenv import load_dotenv
import requests
from django.shortcuts import render, redirect
from .forms import NewsForm
import firebase_admin
from firebase_admin import credentials, firestore, storage
from google.cloud import storage
import os
from django.http import HttpResponseServerError,JsonResponse
load_dotenv()
firebase_admin_creds = os.environ.get('FIREBASE_ADMINSDK_JSON')

if firebase_admin_creds:
    try:
        cred_dict = json.loads(firebase_admin_creds)
        cred = credentials.Certificate(cred_dict)
        firebase_admin.initialize_app(cred, {
            'storageBucket': 'news-88c9e.appspot.com'
        })
        print("Firebase initialized successfully")
    except Exception as e:
        print(f"Failed to initialize Firebase: {str(e)}")
else:
    raise Exception("Firebase Admin SDK JSON not found in environment variables")

NEWS_API_KEY = os.getenv('NEWS_API_KEY')

def get_bitcoin_news(request):
    if not NEWS_API_KEY:
        return JsonResponse({'error': 'API key not found'}, status=500)

    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': 'bitcoin',
        'apiKey': NEWS_API_KEY
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({'error': 'Failed to fetch news'}, status=response.status_code)
    

IMGUR_CLIENT_ID = os.getenv('IMGUR_CLIENT_ID')

import time

def upload_image_to_imgur(image):
    url = "https://api.imgur.com/3/upload"
    headers = {
        'Authorization': f'Client-ID {IMGUR_CLIENT_ID}'
    }
    files = {
        'image': image.read()
    }
    retries = 3
    for attempt in range(retries):
        response = requests.post(url, headers=headers, files=files)
        if response.status_code == 200:
            return response.json()['data']['link']
        elif response.status_code == 503:  # Service Unavailable
            print(f"Imgur service unavailable. Retry {attempt + 1}/{retries}")
            time.sleep(5)  # Wait for 5 seconds before retrying
        else:
            # Log the error for debugging
            print(f"Imgur upload failed: {response.status_code}, {response.text}")
            raise Exception('Failed to upload image to Imgur')
    raise Exception('Failed to upload image to Imgur after multiple attempts')


def upload_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form locally but don't commit to the database yet
            news_instance = form.save(commit=False)
            
            # Upload the image to Imgur
            image = request.FILES['image']
            try:
                image_url = upload_image_to_imgur(image)
            except Exception as e:
                print(f"Error uploading image: {str(e)}")  # Log the error
                return JsonResponse({'error': str(e)}, status=400)
            
            # Save the public URL of the image to the Firestore document
            db = firestore.client()
            doc_ref = db.collection('news').document()
            doc_ref.set({
                'heading': news_instance.heading,
                'imageURL': image_url,
                'shortArticle': news_instance.article_text
            })
            return JsonResponse({'message': 'News created successfully'})
        else:
            return JsonResponse({'error': 'Invalid form data'}, status=400)
    else:
        form = NewsForm()
    return render(request, 'newsupload.html', {'form': form})


import requests

def check_network_connectivity():
    try:
        response = requests.get('https://www.google.com')
        if response.status_code == 200:
            print("Internet access is available")
        else:
            print(f"Internet access failed with status code: {response.status_code}")
    except Exception as e:
        print(f"Failed to access the internet: {str(e)}")

check_network_connectivity()
