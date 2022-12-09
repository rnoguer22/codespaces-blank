from collections import Counter

l = [1,2,3,4,1,2,3,1,2,1]
Counter(l)
Counter({1: 4, 2: 3, 3: 2, 4: 1})
Counter("palabra")
Counter({'a': 3, 'b': 1, 'l': 1, 'p': 1, 'r': 1})
animales = "gato perro canario perro canario perro"
c = Counter(animales.split())
print(c)
Counter({'canario': 2, 'gato': 1, 'perro': 3})
