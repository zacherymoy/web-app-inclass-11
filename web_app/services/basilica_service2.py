#1st version Mike ran
# Tried doing this but not working. 

import basilica

import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BASILICA_API_KEY")

with basilica.Connection(API_KEY) as c:
    embeddings = c.embed_sentences(["Hello world!", "How are you?"])
    print("----------")
    print(list(embeddings)) # [[0.8556405305862427, ...], ...]