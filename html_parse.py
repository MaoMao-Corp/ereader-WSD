from pprint import pprint
from bs4 import BeautifulSoup
from maps import stardict, POS_DOBLE, DICT_TO_SIMPLE, POS_SET

def is_entry(b, p) -> bool:
    if "><b>Syn." not in p.get_text(): print(word)
    return b and (b.get_text(strip=True)==word.capitalize() or b.get_text(strip=True).endswith(".")) and "><b>Syn." not in p.get_text()

def is_new_pos(b) -> bool:
    return b.get("style") and "color: #00b" in b["style"] and b.string and word.capitalize() in b.string

def add_entry(dic,pos,p):
    if pos not in dic: dic[pos] = []
    dic[pos].append(p)

    

def get_definitions(word:str):
    html = stardict[word] 
    soup = BeautifulSoup(html, "html.parser")

    entries = {}
    
    curr_pos = "unk"
    for p in soup.find_all("p"):
        b = p.find("b", recursive=False)
        if is_entry(b, p):
            if is_new_pos(b):
                try:
                    pos = p.find("i", style=lambda v: v and "color: #a00" in v).get_text(strip=True).replace("&","&amp;")
                except Exception as e:
                    pos = "unk"
                if pos in POS_DOBLE: 
                    l_pos = POS_DOBLE[pos]
                    curr_pos = []
                    for p in l_pos:
                        if p in POS_SET: curr_pos.append(p)
                        else:curr_pos.append(DICT_TO_SIMPLE[p])

                elif pos in POS_SET: current_pos = pos

                else:   curr_pos = DICT_TO_SIMPLE[pos]
            
            if type(curr_pos)==list: 
                for cp in curr_pos:
                    add_entry(entries,cp, p)
            else: add_entry(entries, curr_pos, p)

    return entries

if __name__ == "__main__":
    """
    word = input("word: ")
    """
    for word in stardict.keys():
        d = get_definitions(word)
    quit()
    d = get_definitions(word)

    for k,v in d.items():
        print(k, f": {len(v)}")
