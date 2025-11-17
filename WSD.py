from maps import DICT_TO_SIMPLE, POS_DOBLE
from pystardict import Dictionary
import json
import re

count=0

def load_dict(ifo_path: str):  return Dictionary(ifo_path)


def fetch_dictionary_entries(word: str, dictionary) -> list[dict]:
    """
    Fetch definitions using pystardict.
    """
    entries = []
    
    try:
        # Look up word
        response = dictionary[word]

        pos = split_PoS(word, response)

        return pos
        #definitions = re.findall(r">(:?\d\.<\/b>.+?)<\/p", response) 
       
        """
        senses = [re.sub("<.+?>", "", d) for d in definitions]

        
        print(senses)
        quit()
        # pystardict returns bytes, decode to string
        if isinstance(definitions, bytes):
            definitions = definitions.decode('utf-8')
        
        # Split multiple definitions if present
        # (format varies by dictionary)
        definition_list = split_definitions(definitions)
        
        for definition in definition_list:
            entries.append({
                'word': word,
                'definition': definition
            })
        """
    
    except KeyError:
        print(word)
        pass
    return pos    

def split_PoS(word:str, definitions: str)-> dict[str]:
    "Split the definitions by POS"
    pos = []
    try:
        section_pattern = f'<b style="color: #00b">{word.capitalize()}'
        pos_pattern = r'<i style="color: #a00">(:?.+?)</i>'
        
        definitions_section = definitions.split(section_pattern)[1:]
        
        print(len(definitions_section))
        for i, sect in enumerate(definitions_section):
            _ = re.findall(pos_pattern, sect)[0]

            if _ in POS_DOBLE: 
                pos.append([DICT_TO_SIMPLE[p] for p in POS_DOBLE[_]])
            else:
                pos.append(DICT_TO_SIMPLE[_])
        print(pos) 
        dict_pos = {}
        for i, element in enumerate(pos):
            if type(element)==list:
                for p in element:
                    if p not in dict_pos:
                        dict_pos[p]=[]
                    dict_pos[p].append(definitions_section[i])
            else:
                if element not in dict_pos:
                    dict_pos[element] = []
                dict_pos[element].append(definitions_section[i])
        
        print(json.dumps(dict_pos, indent=4))

        dict_pos = clean_dict_pos(dict_pos)
        return dict_pos
    except Exception as e:
        print(f"{e} AT", word)
    
    return pos


def clean_dict_pos(dic):
    clean_dict = {}

    for k, list_ in dic.items():
        clean_dict[k]=[]
        for text in list_:
            





if __name__=="__main__":
    our_dict = load_dict("./dict/stardict")
    word = "abandon"

    np = fetch_dictionary_entries(word, our_dict)
    print(np)
