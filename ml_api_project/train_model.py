import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import joblib

# Load the CSV and fix column names
df = pd.read_csv("my_dataset.csv", encoding="utf-8-sig")
df.columns = df.columns.str.strip().str.replace('\ufeff', '')  # Remove BOM and whitespace

# Debug: Check column names
print("Loaded columns:", df.columns.tolist())

# Convert features to numeric (in case of any issues) and drop rows with missing values
df["tail_length"] = pd.to_numeric(df["tail_length"], errors="coerce")
df["ear_size"] = pd.to_numeric(df["ear_size"], errors="coerce")
df = df.dropna(subset=["tail_length", "ear_size", "breed"])

# Visualize the dataset
sns.scatterplot(data=df, x="tail_length", y="ear_size", hue="breed")
plt.title("Dog Breed Classification")
plt.xlabel("Tail Length")
plt.ylabel("Ear Size")
plt.grid(True)
plt.show()

# Prepare features and labels
X = df[["tail_length", "ear_size"]]  # Features
y = df["breed"]                      # Target label

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a K-Nearest Neighbors classifier
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# Evaluate the model
accuracy = model.score(X_test, y_test)
print(f"Model Accuracy: {accuracy:.2f}")

# Save the trained model to a file
joblib.dump(model, "model.pkl")
print("Model saved as model.pkl")
