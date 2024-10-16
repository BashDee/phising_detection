from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import JsonResponse
import joblib

# Load the KNN model
knn_model = joblib.load('detection/knn_phishing_model.pkl')

@csrf_exempt  # Disable CSRF protection
@api_view(['POST'])  # Only allow POST requests
def predict_phishing(request):
    features = request.data.get('features', [])
    if len(features) != 4:
        return JsonResponse({"error": "Exactly 4 features are required."}, status=400)

    try:
        prediction = knn_model.predict([features])[0]
        result = "Phishing" if prediction == 1 else "Legitimate"

        # Debugging: Log the prediction and features
        print(f"Features: {features}, Prediction: {prediction}")

        return JsonResponse({'result': result})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
