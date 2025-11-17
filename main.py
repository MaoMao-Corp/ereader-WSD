from PoS import get_pos
from WSD import get_sense

def main(sentence: str, target: int, dict_path:str):

    pos_sentence = get_pos(sentence)

    pos_target = pos_sentence[target]
    print(pos_target)

    sense = get_sense(pos_target, dict_path)




if __name__=="__main__":
    sentence = "Let's bench for him for the next game"
    target = 2
    main(sentence, target, "./")
