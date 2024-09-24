# views.py

import pandas as pd
from django.shortcuts import render
from .forms import UploadFileForm
from .models import User
from .utils import calculate_similarity

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            df = pd.read_excel(file)

            # Process each row in the dataframe
            for index, row in df.iterrows():
                User.objects.create(
                    username=row['Username'],
                    interests=row['Interests'],
                    partner_preferences=row['Partner Preferences'],
                    event_preferences=row['Event Preferences']
                )

            # Calculate compatibility scores for each user
            users = list(User.objects.all())
            user_top_10_compatibility = {}
            for user1 in users:
                compatibility_scores = {}
                for user2 in users:
                    if user1 != user2:  # Skip self
                        score = calculate_similarity(user1, user2)
                        compatibility_scores[user2.username] = score

                # Remove self-match entry before sorting
                compatibility_scores.pop(user1.username, None)

                # Convert the dictionary back to a list of tuples and sort it
                compatibility_scores = sorted(compatibility_scores.items(), key=lambda x: x[1], reverse=True)
                top_10_scores = compatibility_scores[:10]  # Select the top 10 scores
                
                # Store the top 10 scores for the user
                user_top_10_compatibility[user1.username] = top_10_scores

            return render(request, 'match_result.html', {'user_top_10': user_top_10_compatibility})
    else:
        form = UploadFileForm()
    
    return render(request, 'match_upload.html', {'form': form})