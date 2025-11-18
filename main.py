from html_parse import get_definitions
from PoS import get_pos
from helper import filter_by_pos
from WSD import  sentence2vec, cos_similarity


def main(sentence: str, target: int):

    pos = get_pos(sentence, target)
    word = sentence.split(" ")[target]

    entries:dict = get_definitions(word)
    entries:list[str] = filter_by_pos(entries, pos) 
    
    all = [sentence]
    all.extend(entries)

    embeddings = sentence2vec(all)
    embed_context = embeddings[0]
    embed_entries = embeddings[1:]

    scores = cos_similarity(embed_context, embed_entries)
    
    rank = []
    for entry, score in zip(entries, scores):
        rank.append((entry, float(score)))
    
    # Sort by score (highest first)
    rank = sorted(rank, key=lambda x: x[1], reverse=True)


    for entry in rank:
        print(entry[0], "score: ", entry[1])
        print("------------")

if __name__=="__main__":
    sentence = "The skier slid down the snow bank"
    target = 6
    main(sentence, target)
