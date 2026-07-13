import pickle
import nltk

nltk.download("punkt")
model = pickle.load(
    open("model.pkl","rb")
)

vectorizer = pickle.load(
    open("vectorizer.pkl","rb")
)
def generate_summary(text):
    sentences = (nltk.sent_tokenize(text))
    important_sentences = []
    for sentence in sentences:
        features = (vectorizer.transform([sentence]))
        prediction = (model.predict(features)[0])
        if prediction == 1:
            important_sentences.append(sentence)
    summary = " ".join(important_sentences[:8])
    return summary