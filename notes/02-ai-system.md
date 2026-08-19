# AI System

## [EN]

```
AI SYSTEM
├── MODEL
│   ├── Transformer
│   ├── LLM
│   └── Embedding
├── DATA
│   ├── Dataset
│   ├── Retrieval
│   └── Documents
└── COMPUTE
    ├── GPU
    ├── CPU
    └── Memory

INFERENCE
    ↓
CONTEXT
    ├── RAG
    ├── Memory
    └── Tools
    ↓
AGENT
    ↓
EVALUATION
    ↓
OBSERVABILITY
    ↓
PRODUCTION
```

Each term answers three questions:
1. What is this?
2. Why does it exist?
3. Which problem does it solve?

This exercise is the most important part of today.

**AI SYSTEM**
What is it?
→ An end-to-end application that combines model, data, and compute to produce useful outputs.
Why does it exist?
→ A model call alone is not a product; it must work as a reliable system.
Which problem does it solve?
→ Turning a model into something that can be used, monitored, and trusted in the real world.

**MODEL**
What is it?
→ The learned component that maps inputs to outputs.
Why does it exist?
→ The system needs a part that can generalize to new inputs instead of following only hard-coded rules.
Which problem does it solve?
→ Producing intelligent behavior without writing a rule for every case.

**Transformer**
What is it?
→ A neural architecture that processes sequences with an attention mechanism.
Why does it exist?
→ Earlier sequence models were slow and weak at long-range context.
Which problem does it solve?
→ Modeling long sequences efficiently and in parallel.

**LLM**
What is it?
→ A large language model trained on massive text to understand and generate language.
Why does it exist?
→ Smaller models were not general enough for open-ended language tasks.
Which problem does it solve?
→ Handling many language tasks with one model instead of a separate model per task.

**Embedding**
What is it?
→ Converting text into a numerical vector.
Why does it exist?
→ To calculate semantic similarity.
Which problem does it solve?
→ Finding semantically similar content even when the words are not exactly the same.

**DATA**
What is it?
→ The information the system learns from, retrieves, and reasons over.
Why does it exist?
→ Models cannot be useful without information to train on or look up.
Which problem does it solve?
→ Grounding AI behavior in facts and examples instead of unsupported guesses.

**Dataset**
What is it?
→ A structured collection of examples used to train, tune, or evaluate a model.
Why does it exist?
→ Learning and measurement require organized examples.
Which problem does it solve?
→ Giving the model something consistent to learn from and be scored against.

**Retrieval**
What is it?
→ Finding the most relevant pieces of information for a query.
Why does it exist?
→ The model cannot store every fact in its weights.
Which problem does it solve?
→ Getting the right documents into context at the right time.

**Documents**
What is it?
→ Source files or records that contain the knowledge the system should use.
Why does it exist?
→ Real knowledge lives outside the model, in files, tickets, and databases.
Which problem does it solve?
→ Giving retrieval something concrete to search over.

**COMPUTE**
What is it?
→ The hardware resources that run training and inference.
Why does it exist?
→ Neural networks need large amounts of numerical computation.
Which problem does it solve?
→ Making model execution fast enough and large enough to be useful.

**GPU**
What is it?
→ A processor optimized for massive parallel math.
Why does it exist?
→ Matrix operations in neural nets are too slow on a CPU at scale.
Which problem does it solve?
→ Training and serving large models in a reasonable time.

**CPU**
What is it?
→ A general-purpose processor for orchestration, I/O, and lighter compute.
Why does it exist?
→ Not every task is a giant matrix multiply; the system still needs a controller.
Which problem does it solve?
→ Running application logic, retrieval, and coordination around the model.

**Memory (Compute)**
What is it?
→ RAM and device memory that hold model weights, activations, and data in flight.
Why does it exist?
→ Weights and context must live in fast storage while they are used.
Which problem does it solve?
→ Fitting the model, batch, and context into hardware so the job can run.

**INFERENCE**
What is it?
→ Running a trained model to produce an output for a new input.
Why does it exist?
→ Training is not the product; answering live requests is.
Which problem does it solve?
→ Turning learned weights into a response at request time.

**CONTEXT**
What is it?
→ The information placed around the prompt so the model can answer this request well.
Why does it exist?
→ The model only sees what fits in its current window.
Which problem does it solve?
→ Supplying the right instructions, history, and retrieved facts before generation.

**RAG**
What is it?
→ Retrieving external knowledge and inserting it into the prompt before generation.
Why does it exist?
→ Model knowledge is frozen and incomplete.
Which problem does it solve?
→ Reducing hallucination by grounding answers in documents.

**Memory (Agent)**
What is it?
→ Stored state that persists across turns or sessions.
Why does it exist?
→ Context windows are temporary and fill up.
Which problem does it solve?
→ Remembering user preferences, past actions, and results over time.

**Tools**
What is it?
→ External functions or APIs the system can call, such as search, code, or databases.
Why does it exist?
→ Text generation alone cannot fetch live data or take actions.
Which problem does it solve?
→ Letting the model get fresh information and affect the world.

**AGENT**
What is it?
→ A loop that plans, uses tools, and takes multiple steps toward a goal.
Why does it exist?
→ One-shot generation cannot complete multi-step work.
Which problem does it solve?
→ Completing tasks that require decisions, retries, and tool calls.

**EVALUATION**
What is it?
→ Measuring quality against defined tests and criteria.
Why does it exist?
→ You cannot improve what you do not measure.
Which problem does it solve?
→ Knowing whether the system is accurate, safe, and good enough to ship.

**OBSERVABILITY**
What is it?
→ Logs, traces, and metrics that show what the live system is doing.
Why does it exist?
→ Failures in production are otherwise invisible.
Which problem does it solve?
→ Debugging latency, cost, quality drift, and unexpected behavior.

**PRODUCTION**
What is it?
→ The deployed system serving real users under real constraints.
Why does it exist?
→ A notebook demo is not a product.
Which problem does it solve?
→ Running reliably at scale with cost, latency, safety, and uptime limits.

## [TUR]

```
AI SYSTEM
├── MODEL
│   ├── Transformer
│   ├── LLM
│   └── Embedding
├── DATA
│   ├── Dataset
│   ├── Retrieval
│   └── Documents
└── COMPUTE
    ├── GPU
    ├── CPU
    └── Memory

INFERENCE
    ↓
CONTEXT
    ├── RAG
    ├── Memory
    └── Tools
    ↓
AGENT
    ↓
EVALUATION
    ↓
OBSERVABILITY
    ↓
PRODUCTION
```

Her terim üç soruyu cevaplar:
1. Bu nedir?
2. Neden var?
3. Hangi problemi çözüyor?

Bu egzersiz bugünün en önemli kısmı.

**AI SYSTEM**
Nedir?
→ Model, data ve compute'u birleştirerek işe yarar çıktı üreten uçtan uca uygulama.
Neden var?
→ Tek başına bir model çağrısı ürün değildir; güvenilir bir sistem olarak çalışması gerekir.
Hangi problemi çözüyor?
→ Bir modeli gerçek dünyada kullanılabilir, izlenebilir ve güvenilir hale getirme.

**MODEL**
Nedir?
→ Girdileri çıktılara dönüştüren, öğrenilmiş bileşen.
Neden var?
→ Sistemin yalnızca hard-coded kurallar değil, yeni girdilere genelleyebilen bir parçaya ihtiyacı vardır.
Hangi problemi çözüyor?
→ Her durum için kural yazmadan akıllı davranış üretme.

**Transformer**
Nedir?
→ Sequence verisini attention mekanizmasıyla işleyen neural mimari.
Neden var?
→ Önceki sequence modelleri yavaştı ve uzun mesafeli bağlamda zayıftı.
Hangi problemi çözüyor?
→ Uzun dizileri verimli ve paralel biçimde modelleme.

**LLM**
Nedir?
→ Büyük miktarda metin üzerinde eğitilmiş, dili anlayan ve üreten language model.
Neden var?
→ Daha küçük modeller açık uçlu dil görevleri için yeterince genel değildi.
Hangi problemi çözüyor?
→ Her görev için ayrı model yerine birçok dil görevini tek modelle çözme.

**Embedding**
Nedir?
→ Metni sayısal vektöre dönüştürme.
Neden var?
→ Semantic similarity hesaplayabilmek.
Hangi problemi çözüyor?
→ Kelimeler birebir aynı olmasa bile anlamca benzer içerikleri bulabilmek.

**DATA**
Nedir?
→ Sistemin öğrendiği, retrieve ettiği ve üzerinde akıl yürüttüğü bilgi.
Neden var?
→ Modeller, eğitilecek veya bakılacak bilgi olmadan işe yaramaz.
Hangi problemi çözüyor?
→ AI davranışını tahmine değil, olgulara ve örneklere dayandırma.

**Dataset**
Nedir?
→ Modeli eğitmek, ayarlamak veya değerlendirmek için kullanılan yapılandırılmış örnek koleksiyonu.
Neden var?
→ Öğrenme ve ölçüm düzenli örneklere ihtiyaç duyar.
Hangi problemi çözüyor?
→ Modele tutarlı öğrenecek ve üzerinden skorlanacak bir zemin verme.

**Retrieval**
Nedir?
→ Bir sorgu için en ilgili bilgi parçalarını bulma.
Neden var?
→ Model her gerçeği ağırlıklarında tutamaz.
Hangi problemi çözüyor?
→ Doğru dokümanları doğru anda context'e getirme.

**Documents**
Nedir?
→ Sistemin kullanması gereken bilgiyi içeren kaynak dosyalar veya kayıtlar.
Neden var?
→ Gerçek bilgi modelin dışında, dosyalarda, ticket'larda ve veritabanlarında yaşar.
Hangi problemi çözüyor?
→ Retrieval'ın üzerinde arama yapacağı somut bir kaynak sağlama.

**COMPUTE**
Nedir?
→ Training ve inference'ı çalıştıran donanım kaynakları.
Neden var?
→ Neural network'ler büyük miktarda sayısal hesaplama ister.
Hangi problemi çözüyor?
→ Model çalıştırmayı yeterince hızlı ve yeterince büyük hale getirme.

**GPU**
Nedir?
→ Yoğun paralel matematik için optimize edilmiş işlemci.
Neden var?
→ Neural net'lerdeki matris işlemleri ölçekte CPU'da çok yavaştır.
Hangi problemi çözüyor?
→ Büyük modelleri makul sürede eğitme ve serve etme.

**CPU**
Nedir?
→ Orchestration, I/O ve daha hafif hesap için genel amaçlı işlemci.
Neden var?
→ Her iş dev bir matris çarpımı değildir; sistemin bir denetleyiciye ihtiyacı vardır.
Hangi problemi çözüyor?
→ Modelin etrafındaki uygulama mantığını, retrieval'ı ve koordinasyonu çalıştırma.

**Memory (Compute)**
Nedir?
→ Model ağırlıklarını, aktivasyonları ve anlık veriyi tutan RAM ve cihaz belleği.
Neden var?
→ Ağırlıklar ve context kullanılırken hızlı depolamada durmalıdır.
Hangi problemi çözüyor?
→ Model, batch ve context'i donanıma sığdırarak işin çalışmasını sağlama.

**INFERENCE**
Nedir?
→ Eğitilmiş modeli yeni bir girdi için çalıştırıp çıktı üretme.
Neden var?
→ Training ürün değildir; canlı isteklere cevap vermek üründür.
Hangi problemi çözüyor?
→ Öğrenilmiş ağırlıkları istek anında bir yanıta dönüştürme.

**CONTEXT**
Nedir?
→ Modelin bu isteği iyi cevaplaması için prompt'un etrafına konan bilgi.
Neden var?
→ Model yalnızca o anki penceresine sığanı görür.
Hangi problemi çözüyor?
→ Üretimden önce doğru talimatları, geçmişi ve retrieve edilmiş gerçekleri sağlama.

**RAG**
Nedir?
→ Dış bilgiyi retrieve edip generation'dan önce prompt'a ekleme.
Neden var?
→ Modelin bilgisi donmuş ve eksiktir.
Hangi problemi çözüyor?
→ Cevapları dokümanlara dayandırarak hallucination'ı azaltma.

**Memory (Agent)**
Nedir?
→ Turlar veya oturumlar boyunca kalıcı olan saklı durum.
Neden var?
→ Context pencereleri geçicidir ve dolar.
Hangi problemi çözüyor?
→ Kullanıcı tercihlerini, geçmiş aksiyonları ve sonuçları zaman içinde hatırlama.

**Tools**
Nedir?
→ Sistemin çağırabildiği dış fonksiyonlar veya API'ler; arama, kod, veritabanı gibi.
Neden var?
→ Salt metin üretimi canlı veri çekemez veya aksiyon alamaz.
Hangi problemi çözüyor?
→ Modelin taze bilgi almasını ve dünya üzerinde işlem yapmasını sağlama.

**AGENT**
Nedir?
→ Planlayan, araç kullanan ve bir hedefe doğru birden fazla adım atan döngü.
Neden var?
→ Tek seferlik üretim çok adımlı işi tamamlayamaz.
Hangi problemi çözüyor?
→ Karar, retry ve tool call gerektiren görevleri tamamlama.

**EVALUATION**
Nedir?
→ Kaliteyi tanımlı testler ve ölçütlere göre ölçme.
Neden var?
→ Ölçmediğin şeyi iyileştiremezsin.
Hangi problemi çözüyor?
→ Sistemin doğru, güvenli ve yayınlanacak kadar iyi olup olmadığını bilme.

**OBSERVABILITY**
Nedir?
→ Canlı sistemin ne yaptığını gösteren log, trace ve metrikler.
Neden var?
→ Production'daki hatalar aksi halde görünmez kalır.
Hangi problemi çözüyor?
→ Gecikme, maliyet, kalite kayması ve beklenmeyen davranışı debug etme.

**PRODUCTION**
Nedir?
→ Gerçek kısıtlar altında gerçek kullanıcılara hizmet veren yayınlanmış sistem.
Neden var?
→ Bir notebook demosu ürün değildir.
Hangi problemi çözüyor?
→ Maliyet, gecikme, güvenlik ve uptime sınırları içinde ölçekte güvenilir çalışma.
