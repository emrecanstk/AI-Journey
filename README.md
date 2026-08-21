# AI Journey

> Snapshot **22 Aug 2026** · Calendar **4 / 28 days** · Target **15 Sep 2026**  
> You are here: **`01-mathematics`** (bird’s-eye done) → next: deepen math **or** continue the Transformer path  
> Goal: understand, build, evaluate, and deploy modern AI systems

```
START 19 Aug                         NOW                         TARGET 15 Sep
│████                                  │░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
0%                                   14%                           100%
     foundations + math map
     neuron · token · attention · next-token
```

```mermaid
%%{init: {"theme": "dark", "themeVariables": {"primaryColor": "#1f6feb", "primaryTextColor": "#fff", "lineColor": "#8b949e", "secondaryColor": "#238636", "tertiaryColor": "#161b22"}}}%%
flowchart LR
  S["19 Aug<br/>START"] --> A["20 Aug<br/>Token → Transformer<br/>→ Next token"]
  A --> B["21 Aug<br/>Math map"]
  B --> H["22 Aug<br/>YOU ARE HERE"]
  H -.-> T["15 Sep<br/>TARGET"]

  style S fill:#238636,stroke:#2ea043,color:#fff
  style A fill:#238636,stroke:#2ea043,color:#fff
  style B fill:#238636,stroke:#2ea043,color:#fff
  style H fill:#1f6feb,stroke:#58a6ff,color:#fff
  style T fill:#21262d,stroke:#8b949e,color:#c9d1d9
```

```mermaid
%%{init: {"theme": "dark"}}%%
flowchart TB
  subgraph PLAN["PLAN — 11 modules"]
    direction TB
    M00["00 foundations"]
    M01["01 mathematics"]
    M02["02 neural-networks"]
    M03["03 transformers"]
    M04["04 llms"]
    M05["05 rag"]
    M06["06 agents"]
    M07["07 memory"]
    M08["08 evaluation"]
    M09["09 production"]
    M10["10 research"]
    M00 --> M01 --> M02 --> M03 --> M04 --> M05 --> M06 --> M07 --> M08 --> M09 --> M10
  end

  style M00 fill:#238636,stroke:#2ea043,color:#fff
  style M01 fill:#1f6feb,stroke:#58a6ff,color:#fff
  style M02 fill:#9e6a03,stroke:#d29922,color:#fff
  style M03 fill:#9e6a03,stroke:#d29922,color:#fff
  style M04 fill:#9e6a03,stroke:#d29922,color:#fff
  style M05 fill:#9e6a03,stroke:#d29922,color:#fff
  style M06 fill:#21262d,stroke:#8b949e,color:#8b949e
  style M07 fill:#21262d,stroke:#8b949e,color:#8b949e
  style M08 fill:#21262d,stroke:#8b949e,color:#8b949e
  style M09 fill:#21262d,stroke:#8b949e,color:#8b949e
  style M10 fill:#21262d,stroke:#8b949e,color:#8b949e
```

**Legend:** green = intro done · blue = **you are here** · amber = started (lab / intuition) · grey = not started

```mermaid
%%{init: {"theme": "dark"}}%%
flowchart LR
  subgraph DONE["Built with my own hands"]
    T[Token] --> E[Embedding]
    E --> A[Attention]
    A --> TR[Transformer block]
    TR --> L[Logits]
    L --> P[Probability]
    P --> N[Next token]
  end
  subgraph MATH["Math under it — bird's-eye"]
    V[Vector / Matrix / Dot]
    S[Softmax]
    G[Loss / Gradient / Descent]
  end
  DONE --- MATH

  style T fill:#238636,stroke:#2ea043,color:#fff
  style E fill:#238636,stroke:#2ea043,color:#fff
  style A fill:#238636,stroke:#2ea043,color:#fff
  style TR fill:#238636,stroke:#2ea043,color:#fff
  style L fill:#238636,stroke:#2ea043,color:#fff
  style P fill:#238636,stroke:#2ea043,color:#fff
  style N fill:#238636,stroke:#2ea043,color:#fff
  style V fill:#1f6feb,stroke:#58a6ff,color:#fff
  style S fill:#1f6feb,stroke:#58a6ff,color:#fff
  style G fill:#1f6feb,stroke:#58a6ff,color:#fff
```

### Level now — 0 none · 1 heard it · 2 can explain · 3 technical

Self-score 20 Aug was **20/45**. After 20–21 Aug labs, placement looks like this (not a new quiz):

```
TOKEN              ████████░░  2/3   lab: bert tokenizer
EMBEDDING          ████████░░  2/3   lab: MiniLM + cosine
ATTENTION          ████████░░  2/3   lab: 2x2 self-attention  (was 0)
LLM NEXT-TOKEN     ████████░░  2/3   loop + temperature       (was 0)
TRAINING vs INFER  ████████░░  2/3   locked the split         (was 1)
VECTOR / DOT       ████████░░  2/3   bird's-eye + NumPy 32
SOFTMAX            ████████░░  2/3   7.2 vs 10.0 sharpening
LOSS / GD          ████████░░  2/3   toy descent to ~10
BACKPROP           ████░░░░░░  1/3   idea only, no full net
RAG                ████░░░░░░  1/3   why it works, no system
VECTOR DB          ██████████  3/3   from 20 Aug check
AGENTS             ████████░░  2/3   chatbot vs agent idea
MEMORY / CONTEXT   ████████░░  2/3   distinction
EVALUATION         ████░░░░░░  1/3
LATENCY / PROD     ░░░░░░░░░░  0/3
```

**Still weak (honest):** full backprop, why softmax uses `exp`, real learning rates, latency/production, a real RAG pipeline.

---

## [EN]

Start: 19 August 2026
Target: 15 September 2026

Goal:

Become capable of understanding, building,
evaluating and deploying modern AI systems.

This is no longer only a private study plan.
It is also a public AI engineering learning journey.

## Learning Philosophy

This repository documents my journey into AI engineering.

The goal is not to collect tutorials or reproduce code blindly.

For each concept, I try to understand:

1. What problem does it solve?
2. Why was it invented?
3. How does it work at a high level?
4. Can I build a minimal version?
5. Where is it used in real systems?
6. What are its limitations?
7. What comes next?

All experiments are documented so that another developer
can reproduce and follow the same learning path.

## Working rhythm

Upper bound: 3 hours a day.

- ~30% learning
- ~40% practice
- ~20% connection / research
- ~10% public documentation

If only 1 hour:

- 20 min explanation
- 25 min one mini experiment
- 10 min connections
- 5 min GitHub notes

By 15 September the repo should show history, experiments,
errors, mini implementations, and technical notes — not only "I learned AI".

Module folders (`00-foundations/` … `10-research/`) will later each have
their own `README.md`, `experiments/`, and `notes/`.

## [TUR]

Başlangıç: 19 Ağustos 2026
Hedef tarih: 15 Eylül 2026

Amaç:

Modern AI sistemlerini anlama, inşa etme,
değerlendirme ve yayınlama yetkinliği kazanmak.

Bu artık yalnızca özel bir öğrenme planı değil.
Aynı zamanda public bir AI engineering learning journey.

**Şu an:** 22 Ağu 2026 · takvim **4 / 28 gün** · **01-mathematics** kuşbakışı bitti.  
Yeşil = giriş tamam · mavi = buradasın · amber = lab/sezgi başladı · gri = henüz yok.

## Learning Philosophy

Bu repo AI engineering yolculuğumu belgeler.

Amaç tutorial biriktirmek veya kodu kör kopyalamak değil.

Her kavram için şunu anlamaya çalışırım:

1. Hangi problemi çözüyor?
2. Neden icat edildi?
3. Yüksek seviyede nasıl çalışıyor?
4. Minimal bir sürümünü kurabilir miyim?
5. Gerçek sistemlerde nerede kullanılır?
6. Sınırları neler?
7. Sırada ne var?

Tüm deneyler, başka bir geliştiricinin aynı yolu
yeniden üretebilmesi için belgelenir.

## Working rhythm

Üst sınır: günde 3 saat.

- ~30% öğrenme
- ~40% pratik
- ~20% bağlantı / araştırma
- ~10% public dokümantasyon

Yalnızca 1 saat varsa:

- 20 dk anlatım
- 25 dk tek mini uygulama
- 10 dk bağlantı
- 5 dk GitHub notu

15 Eylül'de repo tarih, deney, hata, mini implementasyon
ve teknik not göstermeli. Yalnızca "AI öğrendim" değil.

Modül klasörleri (`00-foundations/` … `10-research/`) ileride
her biri kendi `README.md`, `experiments/` ve `notes/` yapısına sahip olacak.
