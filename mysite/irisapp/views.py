# Import necessary modules
from django.shortcuts import render
from joblib import load

# Load the pre-trained model from a file
model = load('./savedmodels/irismodel.joblib')

# Define the view function
def predictor(request):
    # Check if the request method is POST (i.e., the form is submitted)
    if request.method == 'POST':
        # Retrieve form data
        sepal_length = request.POST['sepal_length']
        sepal_width = request.POST['sepal_width']
        petal_length = request.POST['petal_length']
        petal_width = request.POST['petal_width']

        # Use the model to predict the iris species
        y_pred = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])

        # Convert the prediction result to the corresponding species name
        if y_pred[0] == 0:
            y_pred = 'Setosa'
        elif y_pred[0] == 1:
            y_pred = 'Verscicolor'
        else:
            y_pred = 'Virginica'

        # Render the main.html template and pass the prediction result
        return render(request, 'main.html', {'result' : y_pred})

    # If the request method is not POST, just render the main.html template
    return render(request, 'main.html')