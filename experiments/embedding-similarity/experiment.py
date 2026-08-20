import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


sentences = [
    "Arabamın motoru bozuldu.",
    "Otomobilimin motorunda problem var.",
    "Bugün hava çok sıcak.",
    "Yapay zeka hakkında çalışıyorum.",
    "Makine öğrenmesi modellerini inceliyorum.",
    "Aracımın motorunda arıza meydana geldi.",
    "Motorlu taşıtımın güç ünitesinde mekanik bir sorun oluştu.",
    "Aracım çalışmıyor.",
    "Bugün arabamı yıkadım.",
]


model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(sentences)
similarity_matrix = cosine_similarity(embeddings)


print("\nCümleler:\n")
for i, sentence in enumerate(sentences):
    print(f"{i}: {sentence}")


print("\nSimilarity Matrix:\n")
for row in similarity_matrix:
    print([round(float(value), 3) for value in row])


print("\nÇiftler:\n")
for i in range(len(sentences)):
    for j in range(i + 1, len(sentences)):
        score = similarity_matrix[i][j]
        print(
            f"{score:.3f} | "
            f"{sentences[i]} "
            f"<-> "
            f"{sentences[j]}"
        )


def cosine_similarity_manual(a, b):
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    return dot_product / (norm_a * norm_b)


score = cosine_similarity_manual(embeddings[0], embeddings[1])
print("\nManual cosine similarity:")
print(score)


print("\nOdak karşılaştırmalar:\n")
focus_pairs = [
    (0, 1, "aynı anlam, farklı kelime (araba / otomobil)"),
    (0, 5, "aynı anlam, farklı kelime (araba / araç + arıza)"),
    (1, 5, "aynı anlam, üçlü motor grubu"),
    (0, 6, "aynı anlam, kelime eşleşmesi neredeyse yok"),
    (0, 7, "anlam yakın: araç çalışmıyor vs motor bozuldu"),
    (7, 8, "aynı kök (araba/araç), farklı anlam: arıza vs yıkamak"),
    (0, 8, "araba kelimesi ortak, anlam farklı"),
    (0, 2, "ilişkisiz: motor vs hava"),
]

for i, j, note in focus_pairs:
    score = float(similarity_matrix[i][j])
    print(f"{score:.3f} | {note}")
    print(f"       {sentences[i]}")
    print(f"       {sentences[j]}\n")
