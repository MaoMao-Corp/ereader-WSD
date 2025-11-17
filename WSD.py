from maps import DICT_TO_SIMPLE, POS_DOBLE
from pystardict import Dictionary
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
    global count
    try:
        section_pattern = f'<p><b style="color: #00b">{word.capitalize()}'
        definitions_section = definitions.split(section_pattern)[1:]

        pos_pattern = r'<i style="color: #a00">(:?.+?)</i>'
        
        pos = []
        try:
            for i, sect in enumerate(definitions_section):
                _ = re.findall(pos_pattern, sect)[0]

                if _ in POS_DOBLE: 
                    multi_pos = POS_DOBLE[_]
                    pos.extend([DICT_TO_SIMPLE[p] for p in multi_pos])
                else:
                    pos.extend([DICT_TO_SIMPLE[_]])

        except Exception as e:
            count+=1
            pass
        return pos
    except IndexError:
        print("INDEX ERROR AT", word)
        return []



if __name__=="__main__":
    our_dict = load_dict("./dict/stardict")
    word = "signal"

    np = fetch_dictionary_entries(word, our_dict)
    print(np)
