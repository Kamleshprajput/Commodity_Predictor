from sentence_transformers import SentenceTransformer
_embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
def get_embedding(text):
    try:
        embedding = _embedding_model.encode(text)
        return embedding

    except Exception as e:
        raise RuntimeError(f"Embedding generation failed: {str(e)}")