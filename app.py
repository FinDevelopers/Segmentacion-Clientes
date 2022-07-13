import json
from clases import Cliente ,Transaccion
  
def readJSON(json_file):
    with open(json_file, 'r') as json_object:
        return json.load(json_object)

obj = readJSON('test.json')
if obj['tipo']== 'BLACK':
    cliente = Cliente.Black(
        obj['nombre'],
        obj['apellido'],
        obj['numero'],
        obj['DNI'],
    )
elif obj['tipo'] == 'GOLD':
    cliente = Cliente.Gold(
        obj['nombre'],
        obj['apellido'],
        obj['numero'],
        obj['DNI'],
    )
elif obj['tipo'] == 'CLASSIC':
    cliente = Cliente.Classic(
        obj['nombre'],
        obj['apellido'],
        obj['numero'],
        obj['DNI'],
    )
else:
    raise Exception(f"No existe el tipo de cliente {obj['tipo']}") 

print(cliente.dni)

#Como se relacionan las clases
#Cual es la relación entre transacción y cuenta
#¿Cuál es el objetivo principal de sprint?
#Que sería razón
#Hay q definir dirección?