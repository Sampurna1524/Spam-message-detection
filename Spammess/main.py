from fastapi import FastAPI
from pydantic import BaseModel
import joblib

model = joblib.load("svm_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

class Message(BaseModel):
    text: str

app = FastAPI()

@app.post("/predict")
def predict(msg: Message):
    tfidf_input = vectorizer.transform([msg.text])
    prediction = model.predict(tfidf_input)
    return {"prediction": "spam" if prediction[0] == 1 else "ham"}
