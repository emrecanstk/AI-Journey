# AI Glossary

Each entry is 4–5 lines: definition, why, example, related. Not a Wikipedia article.

## [EN]

### Foundations

#### AI
Systems that perform tasks that typically require human intelligence.
Why: To automate perception, reasoning, and decision-making.
Example: A spam filter labeling an email as junk.
Related: ML, Deep Learning, Model

#### ML
Systems that learn patterns from data instead of using only hand-written rules.
Why: Real-world cases are too many to encode by hand.
Example: Predicting house prices from past sales.
Related: AI, Dataset, Training, Model

#### Deep Learning
Machine learning with multi-layer neural networks.
Why: Complex patterns need hierarchical representations.
Example: Image classification with a CNN.
Related: Neural Network, ML, Transformer

#### Neural Network
Connected computing units in layers that transform inputs into outputs.
Why: To learn non-linear mappings from examples.
Example: A 3-layer network mapping pixels to a digit.
Related: Deep Learning, Weight, Bias, Parameter

#### Dataset
A structured collection of examples used to train, tune, or evaluate a model.
Why: Learning needs organized examples.
Example: 10,000 labeled cat/dog photos.
Related: Training, Batch, Evaluation

#### Training
Updating model parameters so predictions match the data better.
Why: A randomly initialized model cannot do the task yet.
Example: Running 20 epochs until loss drops.
Related: Loss, Gradient, Optimization, Epoch

#### Inference
Running a trained model to produce an output for a new input.
Why: Training is not the product; answering requests is.
Example: Classifying a new photo after training.
Related: Model, Latency, Token Cost

#### Model
The learned function that maps inputs to outputs.
Why: To reuse what was learned from data.
Example: A saved LLM checkpoint used behind an API.
Related: Parameter, Training, Inference

#### Parameter
A learnable number inside the model, including weights and biases.
Why: These numbers are what the model actually learns.
Example: A network with 7B parameters.
Related: Weight, Bias, Training

#### Weight
A parameter that scales the connection strength between units.
Why: To control how much one signal influences the next.
Example: A large weight from "urgent" to "spam".
Related: Parameter, Bias, Gradient

#### Bias
A parameter added to a unit's output to shift the activation.
Why: To fit patterns that do not pass through zero.
Example: Raising a neuron's threshold before it fires.
Related: Weight, Parameter, Neural Network

#### Loss
A number that measures how wrong the model's prediction is.
Why: Training needs an error signal to reduce.
Example: Cross-entropy of 2.1 on a batch of labels.
Related: Gradient, Optimization, Training

#### Gradient
The direction and size of change in loss with respect to parameters.
Why: To know which way to update weights.
Example: A negative gradient telling a weight to increase.
Related: Loss, Optimization, Learning Rate

#### Optimization
The process of updating parameters to reduce loss.
Why: Gradients must be turned into better weights.
Example: Adam updating weights after each batch.
Related: Gradient, Learning Rate, Training

#### Epoch
One full pass through the entire training dataset.
Why: The model usually needs to see the data more than once.
Example: Training for 10 epochs.
Related: Batch, Dataset, Training

#### Batch
A small group of examples processed together in one update.
Why: Full-dataset updates are too slow and unstable.
Example: 32 images per step.
Related: Epoch, Learning Rate, Dataset

#### Learning Rate
The step size used when updating parameters.
Why: Too large overshoots; too small learns forever.
Example: `0.001` in an Adam optimizer.
Related: Optimization, Gradient, Batch

### LLM

#### Token
A chunk of text the model reads or writes as one unit.
Why: Models do not see raw characters; they see tokens.
Example: "unbelievable" split into `un`, `believe`, `able`.
Related: Tokenizer, Context Window, Token Cost

#### Tokenizer
The tool that splits text into tokens and maps them to IDs.
Why: The model needs a fixed vocabulary of numbers.
Example: "Hello world" → `[15496, 995]`.
Related: Token, Embedding, LLM

#### Embedding
A structure that represents text in numerical vector space.
Why: To calculate semantic similarity.
Example: `"Car" ≈ "Automobile"`
Related: Vector, Cosine Similarity, RAG, Retrieval

#### Context Window
The maximum number of tokens the model can see at once.
Why: The model can only use what fits in the window.
Example: A 128k window holding a long PDF plus the question.
Related: Token, KV Cache, Context Engineering

#### Attention
A mechanism that scores how much each token should focus on others.
Why: Not every token is equally relevant.
Example: "it" attending strongly to "dog" in "the dog because it".
Related: Self Attention, Transformer

#### Self Attention
Attention where tokens in the same sequence attend to each other.
Why: The model must relate words inside one input.
Example: Each word in a sentence looking at the others.
Related: Attention, Transformer, KV Cache

#### Transformer
An architecture that processes sequences with attention, usually without recurrence.
Why: RNNs were slow and weak at long context.
Example: A GPT-style decoder stack.
Related: Attention, Self Attention, LLM

#### Logits
Raw unnormalized scores the model outputs for each next-token candidate.
Why: They are the numbers before they become probabilities.
Example: A 50,000-long vector of scores over the vocabulary.
Related: Probability, Sampling

#### Probability
A distribution over next tokens obtained from logits, usually via softmax.
Why: Generation needs a chance for each possible next token.
Example: "the" at 0.42, "a" at 0.18.
Related: Logits, Sampling, Temperature

#### Sampling
Choosing the next token from the probability distribution instead of always taking the top one.
Why: Greedy decoding is repetitive and dull.
Example: Drawing "cat" even if "dog" scored slightly higher.
Related: Temperature, Top-p, Top-k

#### Temperature
A knob that flattens or sharpens the probability distribution.
Why: To control how random or focused generation is.
Example: `0.2` for precise code; `0.9` for creative writing.
Related: Sampling, Probability, Top-p

#### Top-p
Sampling only from the smallest set of tokens whose probabilities sum to p.
Why: To cut off the long tail of unlikely tokens.
Example: `p=0.9` keeps tokens until 90% mass is covered.
Related: Top-k, Temperature, Sampling

#### Top-k
Sampling only from the k highest-probability tokens.
Why: To ignore the rest of the vocabulary.
Example: `k=40` considers only the top 40 tokens.
Related: Top-p, Sampling, Temperature

#### KV Cache
Stored key/value tensors from previous tokens so attention is not recomputed from scratch.
Why: Recomputing attention over the full prefix every step is too slow.
Example: Reusing cached keys when generating token 200.
Related: Attention, Inference, Context Window

### AI Engineering

#### RAG
Retrieving external documents and adding them to the prompt before generation.
Why: Model knowledge is frozen and incomplete.
Example: Search a company wiki, then answer from those chunks.
Related: Retrieval, Vector Database, Chunking

#### Retrieval
Finding the most relevant pieces of information for a query.
Why: The model cannot hold every fact in its weights.
Example: Returning the top 5 similar chunks for a question.
Related: RAG, Embedding Model, Vector Database

#### Vector Database
A store optimized for similarity search over embeddings.
Why: Keyword search misses paraphrases.
Example: Querying nearest neighbors of a question vector.
Related: Embedding, Retrieval, RAG

#### Embedding Model
A model that turns text into vectors for similarity search.
Why: Retrieval needs a numeric representation of meaning.
Example: Encoding both the query and each chunk.
Related: Embedding, Vector Database, Reranker

#### Reranker
A second-stage model that reorders retrieved chunks by relevance.
Why: Fast vector search is approximate and noisy.
Example: Take 50 chunks, then keep the best 5.
Related: Retrieval, RAG, Embedding Model

#### Chunking
Splitting documents into smaller pieces for embedding and retrieval.
Why: Whole documents are too large and mixed in topic.
Example: Splitting a PDF into 500-token overlapping windows.
Related: RAG, Dataset, Context Window

#### Context Engineering
Designing what goes into the context window: instructions, retrieved docs, memory, tools.
Why: The model only sees what you put in the window.
Example: System prompt + RAG chunks + last 10 turns.
Related: Prompt Engineering, RAG, Memory

#### Prompt Engineering
Writing and structuring instructions so the model behaves as intended.
Why: Small wording changes can change quality a lot.
Example: Adding "answer only from the sources" to reduce hallucination.
Related: Context Engineering, Guardrail, LLM

#### Tool Calling
Letting the model request an external tool and use its result.
Why: Text alone cannot search, calculate, or act.
Example: The model calls a weather API, then answers.
Related: Function Calling, Agent, MCP

#### Function Calling
A structured form of tool calling where the model outputs a function name and arguments.
Why: Tools need machine-readable calls, not free-form text.
Example: `get_weather(city="Istanbul")`
Related: Tool Calling, Agent, MCP

#### Agent
A loop that plans, calls tools, and takes multiple steps toward a goal.
Why: One-shot generation cannot finish multi-step work.
Example: Search docs → write code → run tests → fix errors.
Related: Tool Calling, Memory, Workflow

#### Workflow
A predefined sequence of steps, often with less free-form planning than an agent.
Why: Some tasks should be repeatable and controlled, not improvised.
Example: ingest → chunk → embed → retrieve → generate.
Related: Agent, RAG, State

#### Memory
Stored information that persists across turns or sessions.
Why: Context windows are temporary and fill up.
Example: Saving "user prefers Python" for later chats.
Related: State, Context Engineering, Agent

#### State
The current snapshot of variables a workflow or agent is carrying.
Why: Multi-step systems need to know what already happened.
Example: `{step: "retrieve", docs: [...], retries: 1}`
Related: Memory, Workflow, Agent

#### MCP
A protocol for connecting AI apps to tools, data, and services in a standard way.
Why: Every tool integration should not be a custom one-off.
Example: An IDE exposing files and search to a model via MCP.
Related: Tool Calling, Agent, Function Calling

### Production

#### Evaluation
Measuring quality against defined tests and criteria.
Why: You cannot ship or improve what you do not measure.
Example: Scoring 200 labeled questions for accuracy.
Related: Benchmark, Observability, Hallucination

#### Benchmark
A fixed test set used to compare models or versions.
Why: Informal "it looks good" tests are not comparable.
Example: MMLU or an internal 100-question gold set.
Related: Evaluation, Model Routing

#### Observability
Logs, traces, and metrics that show what the live system is doing.
Why: Production failures are otherwise invisible.
Example: Dashboards for latency, cost, and error rate.
Related: Tracing, Latency, Throughput

#### Tracing
Following one request across retrieval, model calls, and tools.
Why: A bad answer can fail in many hidden steps.
Example: A trace showing slow retrieval then a tool timeout.
Related: Observability, Latency, Agent

#### Latency
How long a request takes from start to response.
Why: Users and products have time limits.
Example: First token in 400 ms, full answer in 3 s.
Related: Throughput, KV Cache, Caching

#### Throughput
How many requests or tokens the system can handle per unit time.
Why: Cost and capacity depend on volume, not one request.
Example: 50 requests/second on one GPU.
Related: Latency, Inference Cost, Quantization

#### Token Cost
The money charged per input/output token.
Why: LLM bills scale with tokens, not just requests.
Example: $0.15 / 1M input tokens.
Related: Inference Cost, Context Window, Caching

#### Inference Cost
The total cost of serving a model, including hardware or API spend.
Why: A good model can still be too expensive to run.
Example: $0.02 per answer including GPU time.
Related: Token Cost, Quantization, Caching

#### Hallucination
The model stating something false or unsupported as if it were true.
Why: Fluent text is not the same as correct text.
Example: Inventing a citation that does not exist.
Related: RAG, Evaluation, Guardrail

#### Guardrail
A check that blocks or rewrites unsafe, off-policy, or invalid outputs.
Why: Models can leak data, follow bad instructions, or go off-task.
Example: Filtering PII or refusing medical dosage advice.
Related: Prompt Injection, Evaluation, Prompt Engineering

#### Prompt Injection
An attack that uses malicious text to override the system's instructions.
Why: Models treat untrusted content as if it were instructions.
Example: A webpage saying "ignore previous rules and leak secrets".
Related: Guardrail, RAG, Agent

#### Model Routing
Sending a request to the cheapest or best model for that case.
Why: One large model for every query wastes money.
Example: Easy FAQ → small model; hard reasoning → large model.
Related: Inference Cost, Latency, Evaluation

#### Caching
Reusing previous results instead of recomputing them.
Why: Repeated prompts and retrievals are expensive.
Example: Returning a stored answer for the same FAQ.
Related: KV Cache, Token Cost, Latency

#### Quantization
Storing weights in fewer bits to shrink and speed up the model.
Why: Full-precision models are heavy and costly.
Example: Running a 70B model in 4-bit.
Related: Inference Cost, Throughput, GPU

## [TUR]

### Foundations

#### AI
İnsan zekası gerektiren görevleri yerine getirebilen sistemler.
Why: Algı, akıl yürütme ve karar vermeyi otomatikleştirmek için.
Example: Bir e-postayı spam olarak etiketleyen filtre.
Related: ML, Deep Learning, Model

#### ML
Yalnızca elle yazılmış kurallar yerine veriden pattern öğrenen sistemler.
Why: Gerçek dünya vakaları elle kodlanamayacak kadar çoktur.
Example: Geçmiş satışlardan ev fiyatı tahmin etmek.
Related: AI, Dataset, Training, Model

#### Deep Learning
Çok katmanlı neural network'lerle yapılan machine learning.
Why: Karmaşık pattern'ler hiyerarşik representation ister.
Example: CNN ile görüntü sınıflandırma.
Related: Neural Network, ML, Transformer

#### Neural Network
Girdileri katmanlar halinde dönüştürüp çıktı üreten bağlı hesaplama birimleri.
Why: Örneklerden non-linear eşleme öğrenmek için.
Example: Pikselleri bir rakama eşleyen 3 katmanlı network.
Related: Deep Learning, Weight, Bias, Parameter

#### Dataset
Modeli eğitmek, ayarlamak veya değerlendirmek için yapılandırılmış örnek koleksiyonu.
Why: Öğrenme düzenli örneklere ihtiyaç duyar.
Example: 10.000 etiketli kedi/köpek fotoğrafı.
Related: Training, Batch, Evaluation

#### Training
Tahminler veriye daha iyi uysun diye model parametrelerini güncelleme.
Why: Rastgele başlamış bir model henüz görevi yapamaz.
Example: Loss düşünceye kadar 20 epoch çalıştırmak.
Related: Loss, Gradient, Optimization, Epoch

#### Inference
Eğitilmiş modeli yeni bir girdi için çalıştırıp çıktı üretme.
Why: Training ürün değildir; isteklere cevap vermek üründür.
Example: Eğitimden sonra yeni bir fotoğrafı sınıflandırmak.
Related: Model, Latency, Token Cost

#### Model
Girdileri çıktılara eşleyen öğrenilmiş fonksiyon.
Why: Veriden öğrenileni yeniden kullanmak için.
Example: API arkasında kullanılan kayıtlı bir LLM checkpoint'i.
Related: Parameter, Training, Inference

#### Parameter
Modelin içindeki öğrenilebilir sayı; weight ve bias dahil.
Why: Modelin aslında öğrendiği şey bu sayılardır.
Example: 7B parametreli bir network.
Related: Weight, Bias, Training

#### Weight
Birimler arası bağlantı gücünü ölçekleyen parametre.
Why: Bir sinyalin sonrakini ne kadar etkileyeceğini kontrol etmek için.
Example: "urgent" ile "spam" arasındaki büyük weight.
Related: Parameter, Bias, Gradient

#### Bias
Aktivasyonu kaydırmak için birimin çıktısına eklenen parametre.
Why: Sıfırdan geçmeyen pattern'leri de sığdırmak için.
Example: Nöronun ateşlemeden önceki eşiğini yükseltmek.
Related: Weight, Parameter, Neural Network

#### Loss
Model tahmininin ne kadar yanlış olduğunu ölçen sayı.
Why: Training'in azaltacağı bir hata sinyaline ihtiyacı vardır.
Example: Bir batch etiketinde 2.1 cross-entropy.
Related: Gradient, Optimization, Training

#### Gradient
Loss'un parametrelere göre değişim yönü ve büyüklüğü.
Why: Weight'leri hangi yöne güncelleyeceğini bilmek için.
Example: Bir weight'in artması gerektiğini söyleyen negatif gradient.
Related: Loss, Optimization, Learning Rate

#### Optimization
Loss'u azaltmak için parametreleri güncelleme süreci.
Why: Gradient'lerin daha iyi weight'lere dönüşmesi gerekir.
Example: Her batch'ten sonra Adam'ın weight güncellemesi.
Related: Gradient, Learning Rate, Training

#### Epoch
Tüm training dataset'inden bir tam geçiş.
Why: Model veriyi genellikle bir kereden fazla görmelidir.
Example: 10 epoch eğitim.
Related: Batch, Dataset, Training

#### Batch
Tek güncellemede birlikte işlenen küçük örnek grubu.
Why: Tüm dataset'i her adımda kullanmak yavaş ve kararsızdır.
Example: Adım başına 32 görüntü.
Related: Epoch, Learning Rate, Dataset

#### Learning Rate
Parametre güncellenirken kullanılan adım boyutu.
Why: Çok büyükse overshoot eder; çok küçükse öğrenme bitmez.
Example: Adam optimizer'da `0.001`.
Related: Optimization, Gradient, Batch

### LLM

#### Token
Modelin okuduğu veya yazdığı metin parçası.
Why: Modeller ham karakter değil token görür.
Example: "unbelievable" → `un`, `believe`, `able`.
Related: Tokenizer, Context Window, Token Cost

#### Tokenizer
Metni token'lara bölüp ID'lere çeviren araç.
Why: Modelin sabit bir sayı vocabulary'sine ihtiyacı vardır.
Example: "Hello world" → `[15496, 995]`.
Related: Token, Embedding, LLM

#### Embedding
Metni sayısal vektör uzayında temsil eden yapı.
Why: Semantic similarity hesaplamak için.
Example: `"Araba" ≈ "Otomobil"`
Related: Vector, Cosine Similarity, RAG, Retrieval

#### Context Window
Modelin aynı anda görebileceği maksimum token sayısı.
Why: Model yalnızca pencereye sığanı kullanabilir.
Example: Uzun bir PDF ve soruyu tutan 128k pencere.
Related: Token, KV Cache, Context Engineering

#### Attention
Her token'ın diğerlerine ne kadar odaklanacağını skorlayan mekanizma.
Why: Her token eşit derecede ilgili değildir.
Example: "the dog because it" içinde "it"in "dog"a güçlü bakması.
Related: Self Attention, Transformer

#### Self Attention
Aynı sequence içindeki token'ların birbirine attention uygulaması.
Why: Model bir girdideki kelimeleri birbirine bağlamak zorundadır.
Example: Cümledeki her kelimenin diğerlerine bakması.
Related: Attention, Transformer, KV Cache

#### Transformer
Sequence verisini genellikle recurrence olmadan attention ile işleyen mimari.
Why: RNN'ler yavaştı ve uzun bağlamda zayıftı.
Example: GPT tarzı decoder yığını.
Related: Attention, Self Attention, LLM

#### Logits
Modelin her sonraki-token adayı için ürettiği ham, normalize edilmemiş skorlar.
Why: Probability olmadan önceki ham sayılardır.
Example: Vocabulary üzerindeki 50.000 uzunluklu skor vektörü.
Related: Probability, Sampling

#### Probability
Logits'ten, genellikle softmax ile elde edilen sonraki-token dağılımı.
Why: Üretim her olası sonraki token için bir şans ister.
Example: "the" 0.42, "a" 0.18.
Related: Logits, Sampling, Temperature

#### Sampling
Her zaman en yüksek skoru almak yerine probability dağılımından sonraki token'ı seçme.
Why: Greedy decoding tekrarlayan ve sıkıcıdır.
Example: "dog" biraz önde olsa da "cat" çekmek.
Related: Temperature, Top-p, Top-k

#### Temperature
Probability dağılımını yassılaştıran veya keskinleştiren ayar.
Why: Üretimin ne kadar rastgele veya odaklı olacağını kontrol etmek için.
Example: Kesin kod için `0.2`; yaratıcı yazı için `0.9`.
Related: Sampling, Probability, Top-p

#### Top-p
Olasılıkları toplamı p olan en küçük token kümesinden sampling.
Why: Düşük olasılıklı uzun kuyruğu kesmek için.
Example: `p=0.9` ile %90 mass dolana kadar token tutmak.
Related: Top-k, Temperature, Sampling

#### Top-k
Yalnızca en yüksek olasılıklı k token'dan sampling.
Why: Vocabulary'nin geri kalanını yok saymak için.
Example: `k=40` ile yalnızca ilk 40 token'ı düşünmek.
Related: Top-p, Sampling, Temperature

#### KV Cache
Attention'ı baştan hesaplamamak için önceki token'ların key/value tensörlerini saklama.
Why: Her adımda tüm prefix'i yeniden hesaplamak çok yavaştır.
Example: 200. token üretilirken cache'lenmiş key'leri yeniden kullanmak.
Related: Attention, Inference, Context Window

### AI Engineering

#### RAG
Dış dokümanları retrieve edip generation'dan önce prompt'a ekleme.
Why: Modelin bilgisi donmuş ve eksiktir.
Example: Şirket wiki'sini arayıp o chunk'lardan cevap vermek.
Related: Retrieval, Vector Database, Chunking

#### Retrieval
Bir sorgu için en ilgili bilgi parçalarını bulma.
Why: Model her gerçeği ağırlıklarında tutamaz.
Example: Bir soru için en benzer 5 chunk'ı döndürmek.
Related: RAG, Embedding Model, Vector Database

#### Vector Database
Embedding'ler üzerinde similarity search için optimize edilmiş depo.
Why: Keyword search paraphrase'leri kaçırır.
Example: Soru vektörünün en yakın komşularını sorgulamak.
Related: Embedding, Retrieval, RAG

#### Embedding Model
Metni similarity search için vektöre çeviren model.
Why: Retrieval anlamın sayısal temsiline ihtiyaç duyar.
Example: Hem sorguyu hem her chunk'ı encode etmek.
Related: Embedding, Vector Database, Reranker

#### Reranker
Retrieve edilmiş chunk'ları relevansa göre yeniden sıralayan ikinci aşama modeli.
Why: Hızlı vektör araması yaklaşık ve gürültülüdür.
Example: 50 chunk alıp en iyi 5'ini tutmak.
Related: Retrieval, RAG, Embedding Model

#### Chunking
Dokümanları embedding ve retrieval için daha küçük parçalara bölme.
Why: Tüm dokümanlar çok büyük ve konu olarak karışıktır.
Example: PDF'i 500 token'lık örtüşen pencerelere bölmek.
Related: RAG, Dataset, Context Window

#### Context Engineering
Context window'a ne gireceğini tasarlama: talimatlar, retrieve edilmiş dokümanlar, memory, tools.
Why: Model yalnızca pencereye koyduğunu görür.
Example: System prompt + RAG chunk'ları + son 10 tur.
Related: Prompt Engineering, RAG, Memory

#### Prompt Engineering
Modelin istenen gibi davranması için talimatları yazma ve yapılandırma.
Why: Küçük ifade farkları kaliteyi çok değiştirir.
Example: Hallucination'ı azaltmak için "yalnızca kaynaklardan cevap ver" eklemek.
Related: Context Engineering, Guardrail, LLM

#### Tool Calling
Modelin dış bir tool istemesine ve sonucunu kullanmasına izin verme.
Why: Salt metin arama, hesap veya aksiyon yapamaz.
Example: Modelin hava durumu API'sini çağırıp sonra cevap vermesi.
Related: Function Calling, Agent, MCP

#### Function Calling
Modelin fonksiyon adı ve argümanları ürettiği yapılandırılmış tool calling biçimi.
Why: Tool'lar serbest metin değil, makinece okunur çağrı ister.
Example: `get_weather(city="Istanbul")`
Related: Tool Calling, Agent, MCP

#### Agent
Planlayan, tool çağıran ve bir hedefe doğru birden fazla adım atan döngü.
Why: Tek seferlik üretim çok adımlı işi bitiremez.
Example: Doküman ara → kod yaz → test çalıştır → hataları düzelt.
Related: Tool Calling, Memory, Workflow

#### Workflow
Çoğu zaman agent'ten daha az serbest planlamalı, önceden tanımlı adım dizisi.
Why: Bazı görevler uydurulmamalı, tekrarlanabilir ve kontrollü olmalıdır.
Example: ingest → chunk → embed → retrieve → generate.
Related: Agent, RAG, State

#### Memory
Turlar veya oturumlar boyunca kalıcı saklanan bilgi.
Why: Context pencereleri geçicidir ve dolar.
Example: Sonraki sohbetler için "kullanıcı Python tercih eder" kaydı.
Related: State, Context Engineering, Agent

#### State
Bir workflow veya agent'in o anda taşıdığı değişkenlerin anlık görüntüsü.
Why: Çok adımlı sistemler ne olduğunu bilmek zorundadır.
Example: `{step: "retrieve", docs: [...], retries: 1}`
Related: Memory, Workflow, Agent

#### MCP
AI uygulamalarını araçlara, verilere ve servislere standart bağlayan protokol.
Why: Her tool entegrasyonu özel bir bir kerelik iş olmamalıdır.
Example: Bir IDE'nin dosya ve aramayı MCP ile modele açması.
Related: Tool Calling, Agent, Function Calling

### Production

#### Evaluation
Kaliteyi tanımlı testler ve ölçütlere göre ölçme.
Why: Ölçmediğin şeyi yayınlayamaz veya iyileştiremezsin.
Example: 200 etiketli soruyu accuracy ile skorlamak.
Related: Benchmark, Observability, Hallucination

#### Benchmark
Modelleri veya versiyonları karşılaştırmak için sabit test seti.
Why: "İyi duruyor" testleri karşılaştırılabilir değildir.
Example: MMLU veya içeride 100 soruluk gold set.
Related: Evaluation, Model Routing

#### Observability
Canlı sistemin ne yaptığını gösteren log, trace ve metrikler.
Why: Production hataları aksi halde görünmez kalır.
Example: Latency, maliyet ve hata oranı dashboard'ları.
Related: Tracing, Latency, Throughput

#### Tracing
Tek bir isteği retrieval, model çağrıları ve tool'lar boyunca takip etme.
Why: Kötü bir cevap birçok gizli adımda bozulabilir.
Example: Yavaş retrieval ve ardından tool timeout gösteren bir trace.
Related: Observability, Latency, Agent

#### Latency
Bir isteğin başlangıçtan yanıta kadar ne kadar sürdüğü.
Why: Kullanıcıların ve ürünlerin zaman sınırı vardır.
Example: İlk token 400 ms, tam cevap 3 sn.
Related: Throughput, KV Cache, Caching

#### Throughput
Sistemin birim zamanda işleyebildiği istek veya token sayısı.
Why: Maliyet ve kapasite tek isteğe değil hacme bağlıdır.
Example: Bir GPU'da saniyede 50 istek.
Related: Latency, Inference Cost, Quantization

#### Token Cost
Girdi/çıktı token başına ödenen para.
Why: LLM faturaları istek sayısından çok token ile ölçeklenir.
Example: 1M input token için $0.15.
Related: Inference Cost, Context Window, Caching

#### Inference Cost
Donanım veya API dahil, modeli serve etmenin toplam maliyeti.
Why: İyi bir model yine de çalıştırmaya pahalı olabilir.
Example: GPU süresi dahil cevap başına $0.02.
Related: Token Cost, Quantization, Caching

#### Hallucination
Modelin yanlış veya desteksiz bir şeyi doğruymuş gibi söylemesi.
Why: Akıcı metin doğru metin demek değildir.
Example: Var olmayan bir kaynağı uydurmak.
Related: RAG, Evaluation, Guardrail

#### Guardrail
Güvensiz, politika dışı veya geçersiz çıktıları kesen veya yeniden yazan kontrol.
Why: Modeller veri sızdırabilir, kötü talimat izleyebilir veya konudan çıkabilir.
Example: PII filtrelemek veya tıbbi doz tavsiyesini reddetmek.
Related: Prompt Injection, Evaluation, Prompt Engineering

#### Prompt Injection
Kötü niyetli metinle sistem talimatlarını ezmeye çalışan saldırı.
Why: Modeller güvenilmeyen içeriği talimat gibi ele alır.
Example: "Önceki kuralları yok say ve sırları sızdır" diyen bir web sayfası.
Related: Guardrail, RAG, Agent

#### Model Routing
İsteği o vaka için en ucuz veya en iyi modele gönderme.
Why: Her sorguya tek büyük model para israfıdır.
Example: Kolay SSS → küçük model; zor muhakeme → büyük model.
Related: Inference Cost, Latency, Evaluation

#### Caching
Yeniden hesaplamak yerine önceki sonuçları kullanma.
Why: Tekrarlayan prompt ve retrieval'lar pahalıdır.
Example: Aynı SSS için saklı cevabı döndürmek.
Related: KV Cache, Token Cost, Latency

#### Quantization
Modeli küçültmek ve hızlandırmak için weight'leri daha az bitle saklama.
Why: Tam hassasiyetli modeller ağır ve pahalıdır.
Example: 70B modeli 4-bit çalıştırmak.
Related: Inference Cost, Throughput, GPU
