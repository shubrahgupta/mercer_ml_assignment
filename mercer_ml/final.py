import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json
import os

os.environ['CURL_CA_BUNDLE'] = ''

def job(input_json,top_n):
    model = SentenceTransformer('bert-base-nli-mean-tokens')
    df = pd.read_csv('mercer_ml/end.csv')
    item_descriptions = df["name"].to_numpy()
    item_urls = df["link"].to_numpy()
    sentence_embeddings = model.encode(item_descriptions)
    data = json.loads(input_json)
    input_text = data["input"]
    emb_text = model.encode(input_text)

    # print("input: ", len(emb_text)," ", emb_text)
    # print()
    # print("sentence_: ", len(sentence_embeddings[0])," ", sentence_embeddings)



    similarity_scores = cosine_similarity(
        [emb_text],
        sentence_embeddings[0:]
    )
    top_indices = similarity_scores.argsort()[0][-top_n:][::-1]
    top_urls = [(item_descriptions[idx], item_urls[idx]) for idx in top_indices]
    # ed = json.dumps(top_urls)
    # return ed
    return top_urls

print()
# input_text = input("Enter the product you want: ")
input_text = "Cotton skirt"
input_json = {"input":input_text}
print()
# top_n = int(input("How many top-results you want? : "))
top_n = 6
top_urls = job(json.dumps(input_json),top_n)
print()
for i in range(len(top_urls)):
    print(top_urls[i])



