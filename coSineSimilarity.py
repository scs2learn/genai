from sklearn.feature_extraction.text import CountVectorizer

# Sample texts
text1 = "Natural language processing is fascinating."
text2 = "I'm intrigued by the wonders of natural language processing."

# Tokenize and vectorize the texts
vectorizer = CountVectorizer().fit_transform([text1, text2]).toarray()
print(vectorizer)

# Calculate cosine similarity
cosine_sim = cosine_similarity(vectorizer[0, :], vectorizer[1, :])

# Cosine Similarity ranges from 0 to 1, a number closer to 1 means that they are more similar
print("Cosine Similarity:")
print(cosine_sim)
