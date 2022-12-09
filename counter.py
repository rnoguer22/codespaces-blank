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



animales = "gato perro canario perro canario perro"
c = Counter(animales.split())

print(c.most_common(1))  # Primeros elemento más repetido
print(c.most_common(2))  # Primeros dos elementos más repetidos
print(c.most_common())   # Elementos ordenadores por repeticiones
[('perro', 3)]
[('perro', 3), ('canario', 2)]
[('perro', 3), ('canario', 2), ('gato', 1)]
l = [10,20,30,40,10,20,30,10,20,10]
c = Counter(l)

print(c.items())        # Registros del contador por clave-valor
print(c.keys())         # Registros del contador por clave
print(c.values())       # Registros del contador por valor

print(sum(c.values()))  # Suma total de elementos del contador

print(list(c))          # Conversión a lista
print(dict(c))          # Conversión a conjunto
print(set(c))           # Conversión a conjunto
#dict_items([(40, 1), (10, 4), (20, 3), (30, 2)])
#dict_keys([40, 10, 20, 30])
#dict_values([1, 4, 3, 2])
