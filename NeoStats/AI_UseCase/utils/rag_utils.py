import os
from models.embeddings import embed
import numpy as np

def load_documents():
    docs = []
    for file in os.listdir("data"):
        with open(f"data/{file}", "r") as f:
            docs.append(f.read())

    return docs

def retrieve_context(query):
    docs = load_documents()
    q_emb = embed(query)
    scores = []
    for doc in docs:
        d_emb = embed(doc)
        score = np.dot(q_emb, d_emb)
        scores.append((score, doc))
    scores.sort(reverse=True)

    return scores[0][1]