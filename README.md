pip install numpy==1.23.5
pip install scikit-learn pandas joblib
pip install djangorestframework




python manage.py runserver
python manage.py makemigrations
python manage.py migrate

curl -X POST http://127.0.0.1:8000/api/predict/ -H "Content-Type: application/json" -d '{"features": [100, 9]}'
