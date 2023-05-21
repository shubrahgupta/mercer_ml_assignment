from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import re
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import pandas as pd

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

def extract_features(corpus):
    vectorizer = TfidfVectorizer()
    features = vectorizer.fit_transform(corpus)
    return features

def compute_similarity(query_features, item_features):
    similarity_scores = cosine_similarity(query_features, item_features)
    return similarity_scores


def find_similar_items(input_text, item_descriptions, item_urls, top_n=5):
    # Preprocess input text
    processed_text = preprocess_text(input_text)
    # Extract features for input text
    input_features = extract_features([processed_text])
    # Extract features for item descriptions
    item_features = extract_features(item_descriptions)
    print(input_features)
    print(item_features)

    # Compute similarity scores
    similarity_scores = compute_similarity(input_features, item_features)
    # Get indices of top-N most similar items
    top_indices = similarity_scores.argsort()[0][-top_n:][::-1]
    # Retrieve URLs of top-N most similar items
    top_urls = [item_urls[idx] for idx in top_indices]
    return top_urls


df = pd.read_csv("final.csv")


input_text = "Women Kurta and Palazzo Set"
item_descriptions = df["name"].to_numpy()
item_urls = df["link"].to_numpy()
# print(len(item_descriptions),len(item_urls))
top_urls = find_similar_items(input_text, item_descriptions, item_urls, 5)

# Print the ranked URLs
for rank, url in enumerate(top_urls, start=1):
    print(f"Rank {rank}: {url}")


