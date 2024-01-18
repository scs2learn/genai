import transformers
from transformers import pipeline
import torch

prompt = "Is python is a pretty simple language?"
embedder = pipeline("feature-extraction", model="bert-base-uncased")
embedded_prompt = torch.tensor(embedder(prompt)[0][0]).unsqueeze(0)

documents = [
    "Python is a versatile programming language.",
    "Python is a easy language to learn.",
    "Python is a difficult language",
    "Python is a pretty simple language",
    "Natural Language is key to AI",
    "Is python is a pretty simple language?"
]

embedded_docs = [torch.tensor(embedder(doc)[0][0]) for doc in documents]

similarities = [float(torch.nn.functional.cosine_similarity(embedded_prompt, d.unsqueeze(0))) for d in embedded_docs]
most_similar_index = similarities.index(max(similarities))
answer = documents[most_similar_index]

print(prompt)
print(similarities)
print(answer)