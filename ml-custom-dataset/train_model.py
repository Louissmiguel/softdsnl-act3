# train_model.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
df = pd.read_csv("my_dataset.csv")

# Visualize data
sns.scatterplot(data=df, x="tail_length", y="ear_size", hue="breed")
plt.title("Dog Dataset")
plt.xlabel("Tail Length (inches)")
plt.ylabel("Ear Size (inches)")
plt.show()

# Features and labels
X = df[["tail_length", "ear_size"]]
le = LabelEncoder()
y = le.fit_transform(df["breed"])

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model and label encoder
joblib.dump(model, "model.pkl")
joblib.dump(le, "label_encoder.pkl")
print("✅ Dog model trained and saved.")
