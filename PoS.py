from nltk import pos_tag, word_tokenize

nltk.download("averaged_perceptron_tagger")
nltk.download("punkt")

def get_pos(sentence:str) -> list[list[str]]:
    """
    Returns the PoS tag of the input
    Args:
        - sentence(str): sentence to tag
    """
    tokens = word_tokenize(sentence)
    return post_tag(tokens)



if __name__ == "__main__":
    stnc = "After the duck ducked under the lead pipe, the soldiers decided to deset their post, deserting nothing behind, while reading the book on bass fishing"

    print(get_pos(stnc))
