from django.test import TestCase
import requests

# Create your tests here.


test_urls = ["https://www.google.com", "https://secure-login.bank.com"]
for url in test_urls:
    features = extract_features(url)
    response = requests.post('http://localhost:8000/predict-phishing/', json={'features': features})
    print(f"URL: {url}, Response: {response.json()}")
