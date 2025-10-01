#!/usr/bin/env python3
import nltk
from nltk.corpus import movie_reviews
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
for res in ['movie_reviews','punkt']:
    try: nltk.download(res, quiet=True)
    except Exception: pass
try: nltk.download('punkt_tab', quiet=True)
except Exception: pass
first_doc_text = ' '.join(list(movie_reviews.words(movie_reviews.fileids()[0])))
tokens = word_tokenize(first_doc_text)
fdist = FreqDist(tokens)
most_common = fdist.most_common(10)
print("Most common words:", most_common)
try:
    import pandas as pd
    import sys
    df = pd.DataFrame(most_common, columns=['token','count'])
    print("\nTop 10 frequency table:\n", df.to_string(index=False))
except Exception: pass
