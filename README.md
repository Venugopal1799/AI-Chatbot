\# 🤖 AI Chatbot with Python, NLTK, and Scikit-learn



A simple but powerful AI chatbot built using Python, Natural Language Processing (NLP), and machine learning. This project reads user input, predicts the intent using a trained ML model, and responds accordingly using predefined intents and responses.



---



\## 🚀 Features



\- Intent classification using `scikit-learn` (Logistic Regression)

\- Natural language preprocessing with `nltk`

\- Tokenization and stemming for input normalization

\- Pattern-based JSON intent file (`intents.json`)

\- Smart response selection based on predicted intent

\- Easy-to-use command-line interface



---



\## 🛠️ Technologies Used



\- Python 3

\- Scikit-learn

\- NLTK

\- NumPy

\- Pickle

\- JSON



---



\## 📁 Project Structure



AI Chatbot/

│

├── chatbot.py # Chat interface script

├── train\_model.py # Training script

├── intents.json # Intent and response definitions

├── chatbot\_model.pkl # Trained ML model

├── vectorizer.pkl # TF-IDF vectorizer

├── tags.pkl # Encoded tags

└── README.md # Project documentation







---



\## 🧠 How It Works



1\. \*\*Train the Model\*\*  

&nbsp;  Run `train\_model.py` to:

&nbsp;  - Preprocess the data from `intents.json`

&nbsp;  - Vectorize patterns using TF-IDF

&nbsp;  - Train a classifier

&nbsp;  - Save the model and vectorizer using `pickle`



2\. \*\*Run the Chatbot\*\*  

&nbsp;  Execute `chatbot.py` to:

&nbsp;  - Load the trained model

&nbsp;  - Accept user input via the terminal

&nbsp;  - Predict intent and return a smart response



---



\## 🧪 Sample Chat



```bash

🤖 Chatbot is ready! (Type 'quit' to exit)



You: hi

Bot: Hello! How can I help you?



You: what can you do?

Bot: I can assist you with general queries. How may I help?



You: quit

Bot: Goodbye! 👋

📦 Installation \& Setup

bash

Copy

Edit

\# 1. Clone the repository or download the files

git clone https://github.com/your-username/ai-chatbot



\# 2. Install dependencies

pip install nltk scikit-learn numpy



\# 3. Download NLTK data

python

>>> import nltk

>>> nltk.download('punkt')



\# 4. Train the model

python train\_model.py



\# 5. Run the chatbot

python chatbot.py

📌 Future Improvements

Add GUI using Tkinter or PyQt



Convert to web app using Flask or Streamlit



Integrate with ChatGPT API for smarter responses



Store conversation logs for analytics



👨‍💻 Author

Venugopal Valupadasu

Aspiring AI Developer | Python Enthusiast | NLP Learner



📃 License

This project is open-source and free to use for educational purposes.



