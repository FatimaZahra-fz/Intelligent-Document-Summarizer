import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

data = pd.read_csv("dataset.csv")
X = data["description"].astype(str)
keywords = [
    "ai",
    "machine",
    "technology",
    "business",
    "science"
]
y = []
for text in X:
    text = text.lower()
    if any(word in text
        for word in keywords
    ):
        y.append(1)
    else:
        y.append(0)
vectorizer = TfidfVectorizer()
X_features = vectorizer.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_features,y,test_size=0.2,random_state=42)
model = MultinomialNB()
model.fit(X_train,y_train)
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test,predictions)
print("Model Accuracy:",accuracy)
pickle.dump(model,
    open("model.pkl","wb")
)
pickle.dump(vectorizer,
    open("vectorizer.pkl","wb")
)
print("Training Completed")