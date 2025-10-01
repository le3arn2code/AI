#!/usr/bin/env python3
import nltk
from nltk.corpus import movie_reviews
try: nltk.download('movie_reviews', quiet=True)
except Exception: pass
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]
print(f"Total number of documents: {len(documents)}")
print("Preview of first document (30 tokens):", ' '.join(documents[0][0][:30]))
