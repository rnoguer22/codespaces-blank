from collections import OrderedDict

n = OrderedDict()
n['uno'] = 'one'
n['dos'] = 'two'
n['tres'] = 'three'

print(n)

n1 = {}
n1['uno'] = 'one'
n1['dos'] = 'two'

n2 = {}
n2['dos'] = 'two'
n2['uno'] = 'one'

# ¿Tienen los mismos elementos y en el mismo orden?
print(n1 == n2)

print("-------------------------------------------------------")
print("TUPLAS CON NOMBRE")
from collections import namedtuple

Persona = namedtuple('Persona','nombre apellido edad')
p = Persona(nombre="Hector",apellido="Costa",edad=27)

print(p)

# Podemos acceder a los elementos como si fueran atributos de un objeto
print(p.nombre)
print(p.edad)

# O utilizando índices como con las tuplas clásicas
print(p[0])
print(p[-1])



### NOS QUEDAMOS POR EL DATATETIME