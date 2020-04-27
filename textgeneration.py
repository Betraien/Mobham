# -*- coding: utf-8 -*-
import json

import gensim
import random
from utilities import * # import utilities.py module

# ============================
# ====== N-Grams Models ======

t_model = gensim.models.Word2Vec.load('full_grams_cbow_300_wiki.mdl')

def get_word(char,vocab):
    return random.choice(vocab[char])

def gen_sentence(word, key, variance=2, diversity=100):
    key+=random.randint(-variance,variance)
    token =clean_str(word).replace(" ","_")
    sentence=word
    for i in range(key):
        most_similar = t_model.wv.most_similar(token, topn=diversity)
        terms=[]
        for term, score in most_similar:
            terms.append(term)
        sentence+=" "+random.choice(terms)
    return sentence.replace("_"," ")+"."
# a b c    ahmed is a good student. but he is not bas. cause he need encouragment.

def generate_paragraph(list,key,variance=2,diversity=100):
    vocab = json.load(open('data.json', 'r'))
    paragraph=""
    print("list",list,len(list))
    for i in list:
        if i == " ":
            paragraph+="\n"
            continue
        c=get_word(i,vocab=vocab)
        print(c)
        paragraph+=gen_sentence(c,key,variance,diversity).replace("\n","")
    return paragraph

def degenerate_paragraph(paragraph):
    print(paragraph)
    sentences=paragraph.split("\n")
    original = []
    for i in sentences:
        for j in i.split("."):
            if len(j) == 0:
                break
            else:
                original.append(j[0])
        original.append(" ")
    print("degenerate",original,len(sentences))
    return original