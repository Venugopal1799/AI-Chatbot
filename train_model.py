import json
import random
import pickle
import numpy as np

# 📌 Import nltk and download 'punkt'
import nltk
nltk.data.path.append("C:/Users/valup/AppData/Roaming/nltk_data")  # Optional but safe
nltk.download('punkt')

from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression




# Load the data
with open("intents.json", "r") as f:
    data = json.load(f)

stemmer = PorterStemmer()
corpus = []
labels = []
all_tags = []

for intent in data['intents']:
    tag = intent['tag']
    all_tags.append(tag)

    for pattern in intent['patterns']:
        # 🔧 Fix: define pattern correctly in the loop
        tokens = pattern.lower().split()
        stemmed = [stemmer.stem(word) for word in tokens]
        sentence = " ".join(stemmed)
        corpus.append(sentence)
        labels.append(tag)



# Convert text to TF-IDF features
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
y = labels

# Train the model
model = LogisticRegression()
model.fit(X, y)

# Save the model and vectorizer
with open("chatbot_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

with open("tags.pkl", "wb") as f:
    pickle.dump(all_tags, f)

print("✅ Model trained and saved successfully!")

