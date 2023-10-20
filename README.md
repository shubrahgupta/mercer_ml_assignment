# mercer_ml_assignment

Clothing Similarity Search
Overview:

The goal of this project is to create a machine learning model capable of receiving text describing a clothing item and returning a ranked list of links to similar items from different websites. Your solution must be a function deployed on Google Cloud that accepts a text string and returns JSON responses with ranked suggestions.



Steps:

1. Collect and preprocess data.

-Use web scraping tools to gather a dataset of clothing item descriptions and their corresponding URLs from multiple e-commerce websites. Ensure that the dataset is balanced and diverse, including various types of clothing from different brands and retailers.

-Preprocess the text data by cleaning it (remove special characters, lowercasing, etc.), and possibly by applying some form of text normalization (like stemming or lemmatization).

2. Measure similarity.

-Develop a method for extracting useful features from the text descriptions. This could involve using techniques like TF-IDF, word embeddings (Word2Vec, GloVe), or more advanced techniques like transformer-based models (BERT, GPT).

-Implement a method to compute the similarity between the input text and the texts in your database. This could be done using methods like cosine similarity or Jaccard similarity.
3. Return ranked results.

-Design a function that accepts a text string, extracts its features, computes similarities with the items in the database, ranks them based on similarity, and returns the URLs of the top-N most similar items.

4. Deploy the function.

-Containerize your application using Docker, then deploy your function on Google Cloud Functions or Google Cloud Run. Your function should accept a JSON payload with the input text and return a JSON response with the ranked list of similar item URLs.


**Our approach: **
Dataset prep:
1. We get web-scraping APIs for flipkart and amazon.
2. In flipkart_scraper.py, we create a flipkart dataset from that API for 3 labels, men cloth, women cloth and kid cloth so as to add diversity.
    That dataset is in flipkart.csv file.
3. Since Amazon web-scraper was not available, we got hold of 3 datasets containing product info, cloths and other info for men cloth, women cloth and kid cloth categories.
    In amazon.py file, we create a useful dataframe from the previous 3 files, and store it in amazon.csv.
4. Now we want to combine the 2 dataframes- amazon and flipkart so as to fetch result from them, which we do in dataset_prep_preprocess.py and store the final dataframe in end.csv, and after preprocessing the dataframe in preprocessed.csv file.


Model decision, training and output:
We choose sentence transformers as it is state-of-the-art and involves less code.
Got weights from hugging face(didnt need to download it myself) [model = SentenceTransformer('bert-base-nli-mean-tokens')]
Encoded both the input text and the item description from the dataframe end.csv into the model, and getting top 5-6 best results with url in the final.py file.



