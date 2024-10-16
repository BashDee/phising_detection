import joblib
from django.http import JsonResponse
from rest_framework.decorators import api_view

# Load the pre-trained KNN model
knn_model = joblib.load('detection/knn_phishing_model.pkl')

@api_view(['GET', 'POST'])  # Allow both GET and POST methods
def predict_phishing(request):
    if request.method == 'GET':
        return JsonResponse({"message": "Send a POST request with features for prediction."})

    # Handle POST request
    features = request.data.get('features', [])
    if len(features) != 2:
        return JsonResponse({"error": "Exactly 2 features are required."}, status=400)

    # Predict using the KNN model
    prediction = knn_model.predict([features])[0]
    result = "Phishing" if prediction == 1 else "Legitimate"

    return JsonResponse({'result': result})
