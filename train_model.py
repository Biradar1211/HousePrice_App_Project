import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
import joblib
from sample_data import create_sample_data

# Step 1: Load data
df = create_sample_data()

# Step 2: One-hot encode 'location'
encoder = OneHotEncoder(handle_unknown='ignore')
location_encoded = encoder.fit_transform(df[['location']]).toarray()  # convert sparse to dense

# Step 3: Combine numerical and encoded features
X = pd.concat([df[['area', 'rooms']], pd.DataFrame(location_encoded)], axis=1)
X.columns = X.columns.astype(str)  # ✅ Ensure all column names are strings
y = df['price']

# Step 4: Train model
model = LinearRegression()
model.fit(X, y)

# Step 5: Save model and encoder
joblib.dump(model, "model.pkl")
joblib.dump(encoder, "encoder.pkl")

print("✅ Model and encoder trained and saved successfully.")
