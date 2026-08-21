from image.pngtransformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")


def show(text):
    tokens = tokenizer.tokenize(text)
    ids = tokenizer.encode(text)
    print("TEXT:", text)
    print("Tokens:", tokens)
    print("Token IDs:", ids)
    print("n_tokens:", len(tokens), "n_ids:", len(ids))
    print()


print("=== 5.1 first sentence ===")
show("Artificial intelligence is changing software.")

print("=== 5.2 different sentences ===")
for text in [
    "Artificial intelligence",
    "Artificially intelligent",
    "I love programming",
    "Programming is fun",
]:
    show(text)

print("=== 5.4 Turkish test ===")
for text in [
    "Yapay zeka öğreniyorum.",
    "Yapay zekâ sistemleri geliştiriyorum.",
    "Bugün Transformer öğreniyorum.",
    "Arabamın motoru bozuldu.",
]:
    show(text)
