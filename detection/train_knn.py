import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Function to extract features from a URL
def extract_features(url):
    url_length = len(url)
    special_chars = sum([1 for char in url if not char.isalnum()])
    has_https = 1 if url.startswith('https') else 0
    suspicious_keywords = 1 if any(keyword in url for keyword in ['login', 'secure', 'account', 'verify', 'bank', 'update']) else 0
    return [url_length, special_chars, has_https, suspicious_keywords]

# Load the dataset
data = pd.read_csv('phishing_dataset.csv')

# Map the target column to binary values 
data['target'] = data['target'].apply(lambda x: 1 if x == 'Other' else 0)

# Check for any missing values 
print(data.isnull().sum())

# Drop any rows with missing values 
data.dropna(inplace=True)

# Example of checking data balance 
print(data['target'].value_counts())

# Extract features for each URL
data['features'] = data['url'].apply(extract_features)

# Prepare the data for training
X = list(data['features'])
y = data['target']  # Assuming 1 for phishing and 0 for legitimate
print(y)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the KNN model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Save the model
joblib.dump(knn, 'knn_phishing_model.pkl')
