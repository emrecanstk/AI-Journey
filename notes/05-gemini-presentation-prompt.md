# Gemini sunum promptu — Day 01

Bu dosyanın tamamını (başlıktan sonraki metni) kopyalayıp Gemini'ye tek mesaj olarak yapıştır.

---

Aşağıdaki görevi yerine getir.

Sen bir eğitim tasarımcısı ve sunum yazarısın.
Sana verilen brifinge göre tek bir kapsamlı slayt destesi hazırla.

------------------------------------------------
ÇIKTI FORMATI
------------------------------------------------

Her slayt için şunları ayrı ayrı yaz:

1. Slayt numarası
2. Slayt başlığı
3. Slaytta görünecek kısa metin
4. Konuşmacı notu (uzun)
5. Varsa diyagram tarifi

Kurallar:

- Dil: slayt yüzeyi Türkçe olsun.
- Teknik terimler İngilizce kalsın. Örnekler: Transformer, Attention, Token, Logits, Residual, Embedding, RAG, ReLU.
- Üslup ders gibi olsun. Wikipedia gibi olmasın.
- Kısa cümleler kullan. Bir slaytta tek fikir olsun.
- 45 ile 70 slayt arası üret. Acele özetleme.
- Lab sayılarını atlama. Aşağıdaki gerçek sayıları kullan. Uydurma.
- Görsel dil: koyu arka plan, monospace diyagram, oklar, kod kutusu.
- Her bölümün başında bir slayt olsun: bu bölümde ne öğreneceksin.
- Sonda şunlar olsun: 5 dakikalık sözlü tekrar scripti. 10 soruluk mini quiz. Cevap anahtarı konuşmacı notunda olsun.

------------------------------------------------
KİTLE VE HEDEF
------------------------------------------------

İzleyen: AI ye yeni başlayan biri.
Dün embedding ve RAG labı yaptı.
Bugün nöron, Transformer ve next-token zincirini ilk kez görüyor.

Süre: 90 ile 120 dakika anlatım.

Amaç: slayt bitince şu iki soruyu cevaplayabilmek.

Soru 1: Transformer neden var?
Soru 2: LLM aslında ne üretir?

Ezberleme yok:

- Activation isimleri ezberletme.
- Q K V isimlerini ezberletme.
- Formülü ezberletme.

Sezgi evet.
Üç aşamayı bilmek evet.
Döngüyü bilmek evet.

------------------------------------------------
ANLATI SIRASI
------------------------------------------------

Bu sırayı bozma.

1. Dünden köprü. Embedding. Cosine. RAG.
2. Bugünün haritası.
3. Tek nöron.
4. Activation. ReLU ve sigmoid. Ezber yok.
5. İki nöron. Representation.
6. Loss ve öğrenme sezgisi. Training döngüsü.
7. Tokenization.
8. Self-attention. Günün kalbi.
9. Transformer block.
10. LLM next-token. Logits. Temperature.
11. Tüm günün tek zincirde birleşimi.
12. Hâlâ bilinmeyenler. Yarın.

------------------------------------------------
ZORUNLU SLAYTLAR
------------------------------------------------

Şu cümleler ayrı ve vurgulu slayt olsun:

1. Kelime eşittir token olmak zorunda değil.
2. Attention tek başına Transformer değildir.
3. Model cümleyi anlayıp cevap yazmaz. Sonraki tokenı seçer.
4. Temperature modeli yeniden eğitmez.

Kod slaytlarında lab kodunu sadeleştirerek göster.
Sayı slaytlarında aşağıdaki gerçek deney sonuçlarını kullan.

------------------------------------------------
BÖLÜM A. DÜNDEN KÖPRÜ
------------------------------------------------

Embedding nedir:
Metni sayı listesine çevirmek.

Dünkü lab:
Model adı: all-MiniLM-L6-v2
İlk şekil: 5 cümle, her biri 384 sayı. Yani (5, 384).
384 bu modelin cümle vektör boyutudur.
Tek bir boyut motor veya hava demek değildir.

Arka plan zinciri:
cümle
sonra tokenizer
sonra Transformer ve attention
sonra pooling
sonra 384 boyutlu embedding

Bu adım inference idi. Training değildi.

Cosine similarity formülü:
dot(a, b) bölü (a nın uzunluğu çarpı b nin uzunluğu)

Okuma:
1 = benzer yön
0 = ilişkisiz
-1 = zıt yön

sklearn ile elle NumPy aynı çıktı verdi.
Cümle 0 ile cümle 1 skoru yaklaşık 0.390

Anlam kelimeye eşit değildir.
Şu çift yaklaşık 0.776:
Arabamın motoru bozuldu.
Motorlu taşıtımın güç ünitesinde mekanik bir sorun oluştu.
Kelime örtüşmesi neredeyse yok.

Şu çift yaklaşık 0.802:
Arabamın motoru bozuldu.
Aracımın motorunda arıza meydana geldi.

Ters örnek. İngilizce MiniLM Türkçe de bozulabildi.
Şu çift yaklaşık 0.823:
Bugün hava çok sıcak.
Bugün arabamı yıkadım.
Muhtemel gürültü: Bugün kelimesi.

Ders:
Embedding modele ve dile bağlıdır.
Evaluation şarttır.

RAG zinciri:
Query
sonra Embedding
sonra Similarity Search
sonra Relevant Documents

Örnek:
Kullanıcı sorusu: Arabamın motoru neden çalışmıyor?
Doküman başlığı: Motor arızalarının temel nedenleri
Kelimeler farklı olsa da vektörler yakın olabilir.

------------------------------------------------
BÖLÜM B. BUGÜNÜN HARİTASI
------------------------------------------------

Günün yolu:

Tokenization
sonra Embedding ve position
sonra Self-attention
sonra Residual ve LayerNorm
sonra Feed Forward
sonra Residual ve LayerNorm

Buna Transformer block denir.
Birçok block üst üste binince LLM omurgası olur.
En sonda logits, softmax, next token gelir.

Dün 384 sayı gördük.
Bugün o sayıların nasıl üretildiğinin iskeletini görüyoruz.

------------------------------------------------
BÖLÜM C. TEK NÖRON
------------------------------------------------

Dosya:
experiments/neural-network-basics/neuron.py

Değerler:
x1 = 2
x2 = 3
w1 = 0.5
w2 = 0.8
bias = 0.1

Hesap:
2 çarpı 0.5 = 1.0
3 çarpı 0.8 = 2.4
artı 0.1
toplam 3.5

Ekran çıktısı 3.5 oldu.
Float gürültüsü: 3.5000000000000004
Öğrenme yok. Sadece ileri formül.

Akış:
inputs
sonra weights
sonra weighted sum
sonra output

Formül:
z = x1 çarpı w1 + x2 çarpı w2 + b

Bu bir nöronun en temel halidir.

------------------------------------------------
BÖLÜM D. ACTIVATION
------------------------------------------------

ReLU:
max(0, x)

z = 3.5 ise ReLU 3.5
bias = -5 ise z = -1.6 ve ReLU 0
Negatif nöron susar.

Sigmoid:
1 bölü (1 + e üzeri eksi x)

sigmoid(-10) yaklaşık 0
sigmoid(0) = 0.5
sigmoid(10) yaklaşık 1

ReLU bir anahtardır. Geçir veya sıfırla.
Sigmoid sayıyı 0 ile 1 arasına sıkıştırır.
Bugün isim ezberi yok.

------------------------------------------------
BÖLÜM E. İKİ NÖRON VE REPRESENTATION
------------------------------------------------

Aynı x1 ve x2 iki nörona gider.
Weightler farklıdır.

Nöron 1:
z1 = 3.5
h1 = 3.5

Nöron 2:
z2 = 2 çarpı -0.3 + 3 çarpı 0.4 + 0.2 = 0.8
h2 = 0.8

h1 ve h2 ham girdi değildir.
Networkün dönüştürdüğü representationdır.

Dün: cümle 384 sayı.
Bugün: mini hali [3.5, 0.8]

Akış:
x
sonra weighted sum
sonra activation
sonra hidden representation

------------------------------------------------
BÖLÜM F. LOSS VE ÖĞRENME
------------------------------------------------

Dosya:
experiments/neural-network-basics/learn.py

Hedef:
input = 2
target = 10
prediction = 6

Squared error:
(6 eksi 10) nin karesi = 16

Loss, ne kadar yanlış olduğunu söyleyen sayıdır.

Sonra weight değişti.
Mini model: prediction = 2 çarpı weight
Hedef yine 10.

Tablo:

weight 0.5    prediction 1    loss 81
weight 1.0    prediction 2    loss 64
weight 1.5    prediction 3    loss 49
weight 2.0    prediction 4    loss 36
weight 2.5    prediction 5    loss 25

Weight değişince prediction değişir.
Prediction değişince loss değişir.
Öğrenmek: loss küçülsün diye parametreyi oynatmak.
weight = 5 olsa prediction 10 olurdu. O adım alınmadı.

Kilit döngü. LLM eğitimi de buradan büyür:

INPUT
sonra MODEL
sonra PREDICTION
sonra LOSS
sonra GRADIENT
sonra PARAMETER UPDATE
sonra tekrar MODEL

Gradient bugün hesaplanmadı.
Gradient, weighti hangi yöne iteceğindir.

------------------------------------------------
BÖLÜM G. TOKENIZATION
------------------------------------------------

Dosya:
experiments/tokenization/experiment.py

Ham string modele giremez.
Yapay zeka öğreniyorum bir stringdir. Matematik değildir.

Akış:
TEXT
sonra TOKENIZER
sonra TOKEN IDs
sonra MODEL

Kullanılan tokenizer:
bert-base-uncased

Örnek cümle:
Artificial intelligence is changing software.

Tokens:
artificial
intelligence
is
changing
software
nokta

Token IDs:
101, 7976, 4454, 2003, 5278, 4007, 1012, 102

101 = CLS
102 = SEP
6 token var. 8 ID var.
Model harf görmez. Tam sayı görür.

Zorunlu kural:
Kelime eşittir token olmak zorunda değil.

Örnek:
Artificially intelligent
parçaları: artificial , ##ly , intelligent
## işareti kelimenin devamı demektir.

Türkçe testi. Bugün derinleşme. Sadece fark et.
bert-base-uncased İngilizce ağırlıklıdır.
Türkçe eklemelidir. WordPiece sonekleri birim olarak bilmez.

öğreniyorum parçaları: og , ##ren , ##iy , ##orum
Arabamın parçaları: arab , ##am , ##ı , ##n
geliştiriyorum parçaları: gel , ##ist , ##iri , ##yo , ##rum

Dünkü bozuk Türkçe similarity skorlarının bir nedeni bu kırılmadır.

Not:
Dosya adı tokenize.py olmamalı.
Python un kendi tokenize modülüyle çakışır.
Doğru ad: experiment.py

------------------------------------------------
BÖLÜM H. SELF-ATTENTION
------------------------------------------------

Dosya:
experiments/attention/self_attention.py

Bu günün en önemli kısmıdır.
Önce problem. Sonra matematik.

Problem cümlesi:
The animal didn't cross the street because it was tired.

it neyi gösteriyor.
İnsan animal der. street demez.
Modelin tokenlar arası ilişkiyi görmesi gerekir.
Attention bunun için vardır.

Temel fikir:
Her token sorar. Benim için diğer tokenlardan hangileri önemli.

it için adaylar:
animal
street
tired
Önemleri farklıdır.

Q K V. İsim ezberi yok. Benzetme:

Query: ben ne arıyorum
Key: bende hangi bilgi var
Value: eğer beni seçersen sana ne veririm

Formül. Bugün ezberleme:
Attention(Q, K, V) = softmax(Q K transpoz bölü kök d_k) çarpı V

Bilmen gereken üç aşama:
Q çarpı K
sonra attention scores
sonra softmax
sonra weighted values yani V ile çarpım

Çekirdek:
Q çarpı K transpoz
sonra scores
sonra scale
sonra softmax
sonra weights
sonra V ile çarp
sonra output

Mini sayısal örnek.
2 çarpı 2 matris.
d_k = 2
Skorlar kök 2 ile ölçeklendi.

Orijinal:
Q birim matris
K birim matris
V satırları [10, 0] ve [0, 20]

Sonuçlar:
scores = [[1, 0], [0, 1]]
scaled yaklaşık [[0.707, 0], [0, 0.707]]
weights yaklaşık [[0.67, 0.33], [0.33, 0.67]]
output yaklaşık [[6.70, 6.60], [3.30, 13.40]]

Softmax köşegeni tam 1 yapmaz.
Token 0 hâlâ çoğunlukla kendi Value sunu alır.
Ama biraz diğerinden karışır.
Bu karışım attentionın kendisidir.
Yani ağırlıklı bilgi aktarımı.

Q deneyleri:

Birinci Q:
[[0.9, 0.1], [0.1, 0.9]]
weights yaklaşık 0.64 ve 0.36
Daha yumuşak.

İkinci Q:
Her satır [0.5, 0.5]
weights 0.50 ve 0.50
output her token için [5, 10]
Yani iki Value nun ortası.

Amaç:
Attentionın kelimeler arasında ağırlıklı bilgi aktarımı yaptığını matematikle hissetmek.
Q değişince alınan V karışımı değişir.

------------------------------------------------
BÖLÜM I. TRANSFORMER BLOCK
------------------------------------------------

Dosya:
experiments/transformer-block/block.py

Basitleştirilmiş blok:

Token IDs
sonra Embedding
sonra Positional Information
sonra Self Attention
sonra Residual Connection
sonra Layer Normalization
sonra Feed Forward Network
sonra Residual Connection
sonra Layer Normalization

Buna Transformer block denir.
Bir LLM bunların birçoğunun üst üste binmiş halidir.

Zorunlu cümle:
Attention tek başına Transformer değildir.

Transformer şunların birleşimidir:
Attention
artı Feed Forward
artı Normalization
artı Residual Connections

Residual:
output = input + transformation(input)

Demo:
[1, 2, 3] + [0.5, -0.2, 0.1] = [1.5, 1.8, 3.1]
Orijinal sinyal silinmez.
Bu, derin networklerin eğitilmesini kolaylaştıran fikirlerden biridir.

Feed Forward kabaca:
x
sonra Linear
sonra Activation
sonra Linear
sonra output

Demo:
x = [1, -2, 0.5]
Linear ve ReLU sonrası [1, 0, 0.5, 0]
Negatif kanal kapandı.
İkinci Linear sonrası [1, 0, 0.5]

------------------------------------------------
BÖLÜM J. NEXT TOKEN, LOGITS, TEMPERATURE
------------------------------------------------

Günün en önemli bağlantısı.

LLM e verilen context:
The cat sat on the

Model cümleyi anlayıp cevap yazmaz.
Görevi şudur:
Bundan sonra hangi token gelme ihtimali daha yüksek.

Örnek dağılım:
mat 0.42
floor 0.21
chair 0.08
table 0.04

mat seçilirse yeni context:
The cat sat on the mat
Döngü tekrar çalışır.

Döngü:
context
sonra Transformer
sonra logits
sonra probabilities
sonra next token
sonra tokenı context e ekle
sonra başa dön

Logit:
Her olası sonraki token için ham skor.

Sonra:
logits
sonra softmax
sonra probabilities

Temperature:
Modeli yeniden eğitmez.
Sadece inference sırasında seçim dağılımını etkiler.

Aynı logits ile demo:

token mat
T 0.5 = 0.776
T 1.0 = 0.565
T 2.0 = 0.411

token floor
T 0.5 = 0.191
T 1.0 = 0.281
T 2.0 = 0.290

token chair
T 0.5 = 0.026
T 1.0 = 0.103
T 2.0 = 0.176

token table
T 0.5 = 0.006
T 1.0 = 0.051
T 2.0 = 0.124

Düşük temperature daha deterministik.
Yüksek temperature daha çeşitli ve rastlantısal.

Günün cümlesi:
LLM anlayıp yazmaz.
Sonraki token için bir olasılık dağılımı üretir.

------------------------------------------------
BÖLÜM K. TEK ZİNCİR
------------------------------------------------

metin
sonra tokenizer yani token ID
sonra embedding ve position
sonra Transformer block veya blocklar
yani attention, residual, FFN, norm
sonra logits
sonra isteğe bağlı temperature
sonra softmax
sonra next token
sonra tekrar

Dünkü embedding bu makinenin bir çıktısıdır. Cümle vektörü.
RAG o vektörleri doküman aramada kullanır.
LLM cevabı ise token token bu döngüyle uzar.

------------------------------------------------
BÖLÜM L. HÂLÂ BİLİNMEYEN
------------------------------------------------

Şunlar bugün kapanmadı:

1. Embedding veya LLM tam olarak hangi loss ve dataset ile eğitildi.
2. Tek vektör boyutunun semantik anlamı. Yoktur.
3. Gradientin sayısal hesabı. Döngüde adı var. Lab yok.
4. LayerNorm matematiği. Multi-head. Positional encoding formülü.
5. top-p ve top-k sampling. Sözlükte var. Bugün lab yok.

Sonraki konular:
positional encoding
multi-head
gerçek gradient
daha iyi tokenizer özellikle Türkçe

------------------------------------------------
KAPANIS
------------------------------------------------

Şunları üret:

1. 8 maddelik bugün eve götür slaytı
2. 20 ile 30 saniyelik tek nefeste anlatım metni
   Konu: Transformer neden var. LLM ne üretir.
3. 10 soruluk quiz
   Cevap anahtarı konuşmacı notunda

Son slaytta şu dosya yollarını yaz:

experiments/neural-network-basics/neuron.py
experiments/neural-network-basics/learn.py
experiments/tokenization/experiment.py
experiments/attention/self_attention.py
experiments/transformer-block/block.py
experiments/embedding-similarity/experiment.py
days/01.md

------------------------------------------------
EK TALİMAT
------------------------------------------------

Slayt başlıklarını clickbait yapma.
Her lab bölümünde üçlük kullan: ne yaptık, ne gördük, ne anlama geliyor.
Diyagram tariflerini ASCII ve oklarla yaz. Slayta çizebileyim.
İngilizce terim ilk geçtiğinde bir Türkçe sezgi cümlesi koy. Sonra terimi İngilizce bırak.
Sayı tablolarını slaytta göster. Yorumu konuşmacı notuna koy.

Şimdi bu brifinge göre slayt destesini üret.
