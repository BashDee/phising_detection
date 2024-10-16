import joblib
from django.http import JsonResponse
from rest_framework.decorators import api_view

# Load the saved KNN model
knn_model = joblib.load('detection/knn_phishing_model.pkl')


@api_view(['POST'])
def predict_phishing(request):
    # Extract features from request data (adjust based on your dataset)
    features = request.data.get('features', [])

    if len(features) != 2:
        return JsonResponse({"error": "Exactly 2 features are required."}, status=400)

    # Predict using the KNN model
    prediction = knn_model.predict([features])[0]

    result = "Phishing" if prediction == 1 else "Legitimate"
    return JsonResponse({'result': result})


