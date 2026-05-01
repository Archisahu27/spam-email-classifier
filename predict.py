# predict.py

import pickle

# Load saved model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def predict_spam(message):
    # Convert text → vector
    message_vector = vectorizer.transform([message])

    # Predict
    prediction = model.predict(message_vector)[0]

    return prediction

if __name__ == "__main__":
    msg = "Congratulations! You won a free ticket"
    print(predict_spam(msg))