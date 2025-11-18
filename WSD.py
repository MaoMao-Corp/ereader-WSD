from sentence_transformers import SentenceTransformer 
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from html_parse import get_definitions 

model = SentenceTransformer("all-MiniLM-L12-v2")

def sentence2vec(sentences:str)-> list[float]:
    if type(sentences) == list:
        return model.encode(sentences)
    else: return model.encode([sentences])[0]

def cos_similarity(v1,v2) -> float:
    score = cosine_similarity([v1],v2)[0]
    return score

if __name__=="__main__":
    pass
