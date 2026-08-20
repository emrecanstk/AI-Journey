# Semantic Similarity Lab

## [EN]

### Goal

Understand why embeddings are useful for semantic search.

### What I did

- Converted sentences into embeddings.
- Calculated cosine similarity.
- Compared semantically similar sentences.
- Compared unrelated sentences.
- Implemented cosine similarity manually.
- Used embeddings to retrieve relevant documents.

### Key observation

Semantically similar sentences can have different words
but still have similar vector representations.

### Connection to RAG

Query → Embedding → Similarity Search → Relevant Documents

### What I still don't understand

- How is the embedding model trained?
- Why does a particular vector dimension represent what it represents?
- How does the Transformer create these representations?
- What exactly happens inside attention?

### Next

Study:
- Tokenization
- Embeddings
- Attention
- Transformer

## [TUR]

### Goal

Embedding'lerin semantic search için neden işe yaradığını anlamak.

### What I did

- Cümleleri embedding'e çevirdim.
- Cosine similarity hesapladım.
- Anlamca benzer cümleleri karşılaştırdım.
- İlişkisiz cümleleri karşılaştırdım.
- Cosine similarity'yi elle (NumPy ile) yazdım.
- Embedding'leri ilgili dokümanları bulmak için kullandım.

### Key observation

Anlamca benzer cümleler farklı kelimeler kullanabilir
ama yine de benzer vektör temsillerine sahip olabilir.

### Connection to RAG

Query → Embedding → Similarity Search → Relevant Documents

### What I still don't understand

- Embedding modeli nasıl eğitilir?
- Belirli bir vektör boyutu neden tam olarak o şeyi temsil eder?
- Transformer bu temsilleri nasıl üretir?
- Attention'ın içinde tam olarak ne olur?

### Next

Çalışılacak:
- Tokenization
- Embeddings
- Attention
- Transformer
