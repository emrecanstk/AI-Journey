from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

sentences = [
    "Arabamın motoru bozuldu.",
    "Otomobilimin motorunda problem var.",
    "Bugün hava çok sıcak.",
    "Yapay zeka hakkında çalışıyorum.",
    "Makine öğrenmesi modellerini inceliyorum.",
]

model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(sentences)

print("Embedding shape:")
print(embeddings.shape)

print("\nEmbedding örneği:")
print(embeddings[0])
