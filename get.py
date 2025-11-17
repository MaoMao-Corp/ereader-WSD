from pystardict import Dictionary



a = input("word: ")
d = Dictionary("./dict/stardict")

print(d[a].strip())
