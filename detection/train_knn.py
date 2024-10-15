import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load the dataset
data = pd.read_csv('phishing_dataset.csv')

# Verify the content
print(data.head())  # Check the structure of your dataset

# Feature extraction: Create numerical columns from the 'url' field
def extract_features(row):
    url = row['url']
    return len(url), sum(1 for char in url if not char.isalnum())  # Tuple

# Apply feature extraction to create a DataFrame with numerical columns
features = data.apply(lambda row: extract_features(row), axis=1)
features_df = pd.DataFrame(features.tolist(), columns=['url_length', 'special_chars'])

print(features_df.head())  # Check the extracted numerical features

# Convert the 'verified' column to a binary label (1 for 'yes', 0 for 'no')
data['label'] = data['verified'].apply(lambda x: 1 if x == 'yes' else 0)

# Prepare features (X) and labels (y)
X = features_df  # Extracted numerical features
y = data['label']  # Target labels

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the KNN model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Evaluate the model
y_pred = knn.predict(X_test)
print(f'Accuracy: {accuracy_score(y_test, y_pred):.2f}')

# Save the trained KNN model
joblib.dump(knn, 'detection/knn_phishing_model.pkl')
print("Model saved successfully.")
