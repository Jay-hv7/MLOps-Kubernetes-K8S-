import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib 

# Load dataset from external CSV file
url = "https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv"
df = pd.read_csv(url)

print("Columns in the dataset:", df.columns.tolist())

# Prepare features and target variable
X = df[["Pregnancies", "Glucose", "BloodPressure",  "BMI",  "Age"]]
y = df["Outcome"]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# train the RandomForestClassifier model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print("Model training completed.")

# Save the trained model to a file
joblib.dump(model, "random_forest_diabetes_model.pkl")
print("Trained model saved as 'random_forest_diabetes_model.pkl'.")

