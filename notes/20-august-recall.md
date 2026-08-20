# 20 August Recall

01 — Recall yesterday | 20 minutes

Answered from the lab and notes, without looking anything up.

Date: 20 August 2026

## [EN]

### Question 1: What is an embedding?

A list of numbers that represents a piece of text in vector space.

In the lab, `"Arabamın motoru bozuldu."` became 384 numbers. Those numbers are the embedding. They are not the words themselves. They are a position that the model assigns to the meaning of the sentence.

### Question 2: Why do we use embeddings?

So we can compare meaning, not exact words.

`"Arabamın motoru bozuldu."` and `"Motorlu taşıtımın güç ünitesinde mekanik bir sorun oluştu."` share almost no words, but their vectors were close (about 0.776). Keyword search would miss that. Embedding search can still treat them as similar.

### Question 3: What does cosine similarity measure?

How similar the **directions** of two vectors are.

Formula used in the lab: `dot(a, b) / (|a| * |b|)`.

- **1** → same direction, very similar
- **0** → unrelated
- **-1** → opposite direction

It does not measure “how many words overlap”. It measures the angle between two embeddings. A sentence compared with itself is 1.0.

### Question 4: Why do embeddings work in the RAG retrieval stage?

RAG has to find the right documents **before** the model writes an answer.

Flow:

```
Query → Embedding → Similarity Search → Relevant Documents
```

The user may ask `"Arabamın motoru neden çalışmıyor?"` while a document is titled `"Motor arızalarının temel nedenleri..."`. Words differ. Embeddings still put both near each other, so retrieval can pull that document into context. Then generation uses those docs instead of guessing.

### Question 5: How might a model that turns a sentence into an embedding have learned?

I did not train it. `all-MiniLM-L6-v2` was already trained. Our run was **inference**.

A plausible learning goal: show the model many sentence pairs. If two sentences mean the same thing, pull their vectors together. If they mean different things, push them apart. After enough pairs, a new sentence lands near other sentences with similar meaning.

What I still do not know in detail: the exact loss, the exact dataset, and the training steps.

### Question 6: Do you know what the number 384 means?

Yes, at lab level: it is the **size of one sentence vector** for this model.

`embeddings.shape` was `(5, 384)`: 5 sentences, 384 numbers each. MiniLM-L6-v2 was built with a 384-dimensional hidden size.

No: I do not know what dimension 17 or dimension 203 “means” in human language. A single slot is not “motor” or “weather”. Meaning is the whole vector’s position relative to other vectors.

### Question 7: What is the difference between an embedding and a token?

A **token** is a chunk of text the model reads, mapped to an ID.

`"Arabamın motoru bozuldu."` is split into pieces like `Araba`, `motor`, `bozuldu`, then IDs.

An **embedding** is a dense vector of meaning. The Transformer turns those tokens into contextual vectors, then pooling (mean of token vectors in our lab) makes **one** sentence embedding.

Short:

- token = input piece / ID
- embedding = numeric meaning vector

A sentence has many tokens and, after encode, one sentence embedding.

## [TUR]

### Question 1: Embedding nedir?

Metni vektör uzayında temsil eden bir sayı listesi.

Labde `"Arabamın motoru bozuldu."` 384 sayıya dönüştü. Bu sayılar embedding. Kelimelerin kendisi değil. Modelin cümlenin anlamına atadığı bir konum.

### Question 2: Neden embedding kullanıyoruz?

Anlamı karşılaştırmak için; kelimelerin birebir aynı olması şart değil.

`"Arabamın motoru bozuldu."` ile `"Motorlu taşıtımın güç ünitesinde mekanik bir sorun oluştu."` neredeyse hiç aynı kelime paylaşmadı ama vektörleri yakındı (yaklaşık 0.776). Keyword search bunu kaçırır. Embedding search benzer sayabilir.

### Question 3: Cosine similarity ne ölçüyor?

İki vektörün **yönlerinin** ne kadar benzer olduğunu.

Labdeki formül: `dot(a, b) / (|a| * |b|)`.

- **1** → aynı yön, çok benzer
- **0** → ilişkisiz
- **-1** → zıt yön

“Kaç kelime örtüşüyor?” ölçmez. İki embedding arasındaki açıyı ölçer. Bir cümle kendisiyle 1.0 eder.

### Question 4: RAG'in retrieval aşamasında embedding neden işe yarıyor?

RAG, model cevap yazmadan **önce** doğru dokümanları bulmak zorundadır.

Akış:

```
Query → Embedding → Similarity Search → Relevant Documents
```

Kullanıcı `"Arabamın motoru neden çalışmıyor?"` diye sorabilir; doküman başlığı `"Motor arızalarının temel nedenleri..."` olabilir. Kelimeler farklıdır. Embedding ikisini yine yakın koyabilir; retrieval o dokümanı context'e çeker. Generation de tahmin etmek yerine o parçaları kullanır.

### Question 5: Bir cümleyi embedding'e dönüştüren model nasıl öğrenmiş olabilir?

Ben eğitmedim. `all-MiniLM-L6-v2` zaten eğitilmişti. Bizim çalıştırdığımız **inference**.

Mantıklı öğrenme hedefi: modele çok sayıda cümle çifti göstermek. Anlam aynıysa vektörleri yaklaştır. Anlam farklıysa uzaklaştır. Yeterince çiftten sonra yeni bir cümle, benzer anlamdaki cümlelerin yakınına düşer.

Ayrıntısını henüz bilmiyorum: tam loss, tam dataset, tam training adımları.

### Question 6: 384 sayısının ne anlama geldiğini biliyor musun?

Lab seviyesinde evet: bu modelde **bir cümle vektörünün boyutu**.

`embeddings.shape` `(5, 384)` idi: 5 cümle, her biri 384 sayı. MiniLM-L6-v2 384 boyutlu hidden size ile üretilmiş.

Hayır: 17. veya 203. boyutun insan dilinde “ne olduğu”nu bilmiyorum. Tek bir slot “motor” veya “hava” demek değil. Anlam, tüm vektörün diğer vektörlere göre konumu.

### Question 7: Embedding ile token arasındaki fark nedir?

**Token**, modelin okuduğu metin parçasıdır; bir ID'ye çevrilir.

`"Arabamın motoru bozuldu."` `Araba`, `motor`, `bozuldu` gibi parçalara, sonra ID'lere bölünür.

**Embedding**, anlamın yoğun sayı vektörüdür. Transformer token'ları bağlamsal vektörlere çevirir; labde pooling (token vektörlerinin ortalaması) **tek** cümle embedding'i üretir.

Kısa:

- token = girdi parçası / ID
- embedding = sayısal anlam vektörü

Bir cümlede birçok token vardır; encode sonrası bir cümle embedding'i kalır.
