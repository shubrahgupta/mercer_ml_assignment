import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import pandas as pd

# nltk.download('stopwords')
def preprocess_text(text):
    # Remove special characters
    text = re.sub(r"[^\w\s]", "", text)
    # Lowercasing
    text = text.lower()
    # Tokenization (split text into words)
    tokens = text.split()
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    # Stemming
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(token) for token in tokens]
    # Join tokens back into a string
    processed_text = ' '.join(tokens)
    return processed_text

flipkart = pd.read_csv("flipkart.csv")
amazon = pd.read_csv("amazon.csv")

df = pd.concat([flipkart,amazon], join="inner",ignore_index=True)
df.to_csv("final.csv")
for i in range(len(df)):
    a = preprocess_text(df["name"][i])
    df["name"][i] = a
df.to_csv("preprocessed.csv")
print(df.name[0])

