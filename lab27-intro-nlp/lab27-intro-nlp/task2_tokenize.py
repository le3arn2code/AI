#!/usr/bin/env python3
import nltk
from nltk.corpus import movie_reviews
from nltk.tokenize import word_tokenize
for res in ['movie_reviews','punkt']:
    try: nltk.download(res, quiet=True)
    except Exception: pass
try: nltk.download('punkt_tab', quiet=True)
except Exception: pass
first_doc_text = ' '.join(list(movie_reviews.words(movie_reviews.fileids()[0])))
tokens = word_tokenize(first_doc_text)
print("First few tokens:", tokens[:10])
print("Total tokens in first doc:", len(tokens))
