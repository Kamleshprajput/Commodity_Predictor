import os
import numpy as np
from models.embeddings import get_embedding

CHUNKS = []
EMBEDDINGS = []

def split_text(text, chunk_size=400):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])

    return chunks

def load_documents():
    global CHUNKS, EMBEDDINGS
    if CHUNKS:
        return
    for file in os.listdir("data"):
        with open(f"data/{file}") as f:
            text = f.read()
            chunks = split_text(text)
            for chunk in chunks:
                CHUNKS.append(chunk)
                EMBEDDINGS.append(get_embedding(chunk))

def retrieve_context(query, top_k=2):
    load_documents()
    query_embedding = get_embedding(query)
    scores = []
    for i, emb in enumerate(EMBEDDINGS):
        score = np.dot(query_embedding, emb)
        scores.append((score, CHUNKS[i]))
    scores.sort(reverse=True)

    return "\n".join([chunk for _, chunk in scores[:top_k]])