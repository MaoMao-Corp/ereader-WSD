from pystardict import Dictionary
from maps import POS_DOBLE


a = input("word: ")
d = Dictionary("./dict/stardict")

count =0
for k in d.keys():
    for _ in POS_DOBLE:
        if _ in d[k] and d[k].count("n.")>10:
            print(f"--{k}--")
            count+=1
    if count>5: quit()
