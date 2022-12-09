from collections import defaultdict

d = defaultdict(float)  # tipo flotante por defecto
print(d['algo'])
print(d)
0.0
defaultdict(float, {'algo': 0.0})
d = defaultdict(str)  # tipo cadena por defecto
print(d['algo'])
print(d)
''
defaultdict(str, {'algo': ''})
d = defaultdict(object)  # tipo objeto por defecto
print(d['algo'])
print(d)