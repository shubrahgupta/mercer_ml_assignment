import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json

def job(input_json,top_n):
    model = SentenceTransformer('bert-base-nli-mean-tokens')
    df = pd.read_csv('mercer_ml/end.csv')
    item_descriptions = df["name"].to_numpy()
    item_urls = df["link"].to_numpy()
    sentence_embeddings = model.encode(item_descriptions)
    data = json.loads(input_json)
    input_text = data["input"]
    emb_text = model.encode(input_text)



    similarity_scores = cosine_similarity(
        [emb_text],
        sentence_embeddings[0:]
    )
    top_indices = similarity_scores.argsort()[0][-top_n:][::-1]
    top_urls = [item_urls[idx] for idx in top_indices]
    ed = json.dumps(top_urls)
    return ed

input_text = "pant"
input_json = {"input":input_text}
top_n = 5
top_urls = job(json.dumps(input_json),top_n)
print(top_urls)



