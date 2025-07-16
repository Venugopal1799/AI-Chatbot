import json
import random
import pickle
import numpy as np
from nltk.stem import PorterStemmer

# Load model and related files
with open("chatbot_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("tags.pkl", "rb") as f:
    tags = pickle.load(f)

with open("intents.json", "r") as f:
    intents = json.load(f)

stemmer = PorterStemmer()


# ✅ PASTE HERE: Function definitions
def preprocess(text):
    tokens = text.lower().split()
    stemmed = [stemmer.stem(word) for word in tokens]
    return " ".join(stemmed)


def get_response(user_input):
    processed = preprocess(user_input)
    X = vectorizer.transform([processed])
    prediction = model.predict(X)[0]

    # Find matching intent
    for intent in intents["intents"]:
        if intent["tag"] == prediction:
            return random.choice(intent["responses"])

    return "I'm not sure how to respond to that."


# ✅ Then the chatbot loop
print("🤖 Chatbot is ready! (Type 'quit' to exit)\n")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Bot: Goodbye! 👋")
        break
    response = get_response(user_input)
    print("Bot:", response)
