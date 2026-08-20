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


similarity_matrix = cosine_similarity(embeddings)


print("\nCümleler:\n")

for i, sentence in enumerate(sentences):
    print(f"{i}: {sentence}")


print("\nSimilarity Matrix:\n")

for row in similarity_matrix:
    print([round(value, 3) for value in row])
