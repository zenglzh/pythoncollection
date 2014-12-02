'''
Created on 2014-12-2

@author: zenglizhi
'''

import logging
from gensim import corpora, models, similarities

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


documents = ["Shipment of gold damaged in a fire",
            "Delivery of silver arrived in a silver truck",
            "Shipment of gold arrived in a truck"]

texts = [[word for word in document.lower().split()] for document in documents]
print texts
dictionary = corpora.Dictionary(texts)

print dictionary
print dictionary.token2id

corpus = [dictionary.doc2bow(text) for text in texts]

print corpus

tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
for doc in corpus_tfidf:
    print doc




